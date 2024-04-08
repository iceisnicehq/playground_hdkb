#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR"
pwd

domain="ld.yandex.ru"
timeout=300  
elapsed=0
interval=5
minute_counter=0
resolved=0  

while [ $elapsed -lt $timeout ]; do
    lookup_result=$(nslookup "$domain" 2>&1)

    if echo "$lookup_result" | grep -q "Can't find $domain"; then
        echo "Domain $domain does not resolve. Trying again in ${interval}s."
    elif echo "$lookup_result" | grep -q "connection timed out"; then
        echo "Network connection is down. Cannot reach DNS server. Please connect to the internet. Trying again in ${interval}s."
    else
        echo "Domain $domain resolved to an IP address."
        resolved=1
        break
    fi

    sleep $interval
    elapsed=$((elapsed + interval))
    minute_counter=$((minute_counter + interval))

    # Report time left and status update every minute
    seconds_left=$((timeout - elapsed))
    if [ $minute_counter -ge 60 ]; then
        remaining_minutes=$((seconds_left / 60))
        echo "Status update: Still trying to connect. Time left: ${remaining_minutes} minute(s)."
        minute_counter=0
    else
        echo "Time left: ${seconds_left}s."
    fi
done

if [ $resolved -ne 1 ]; then
    echo "Timeout reached. Domain $domain did not resolve."
    exit 1  
fi


# Проверка АД
ad_info=$(id eye 2>/dev/null)
if [[ -z $ad_info ]] || [[ $ad_info == *"no such user"* ]]; then
  echo "Error: not_connected_to_AD (Please launch \"rebind.sh\")"

  cat <<EOF > rebind.sh
#!/bin/bash
echo "Rebinding to AD..."
echo "Enter password for sudo access"
sudo jamf policy -trigger rebind
sudo jamf recon
sudo jamf policy
sudo mdmcheck now
echo "Please lauch hdkb.sh again"
# Самоудаление скрипта rebind.sh
script_path="\$( cd "\$( dirname "\${BASH_SOURCE[0]}" )" &> /dev/null && pwd )/\$(basename "\$0")"
if [ -f "\$script_path" ]; then
    rm -- "\$script_path"
else
    echo "Failed to delete the script: \$script_path"
fi
EOF
  chmod +x rebind.sh
  exit 1
fi


echo "Laptop in AD, proceeding"

#Проверка токена у админа
output=$(sysadminctl -secureTokenStatus admin 2>&1)
status=$(echo "$output" | grep -Eo 'ENABLED|DISABLED')
if [[ "$status" == "ENABLED" ]]; then
    echo "Admin token is enabled"
elif [[ "$status" == "DISABLED" ]]; then
    echo "Admin token is disabled. Please enable manually"
    exit 1
else
    echo "Status is unknown or command failed."
    exit 1
fi

admin_username=$(whoami)
user_login=""

for username in $(dscl . list /Users UniqueID | awk '$2 >= 500 {print $1}'); do
    if [[ "$username" != "$admin_username" ]]; then
        user_login=$username
        break
    fi
done

if [[ -n $user_login ]]; then
    read -p "Is '$user_login' the correct other user account name? (y/n or Enter): " confirmation
    if [[ $confirmation =~ ^([Yy][Ee][Ss]|[Yy])$ ]] || [[ -z $confirmation ]]; then
        echo "Confirmed user account name: $user_login"
    else
        read -p "Please type the correct other user account name: " ad_login
        user_login=$ad_login
        echo "User provided name: $user_login"
    fi
else
    echo "No other user account found. Please type the user account name: "
    read ad_login
    user_login=$ad_login
    echo "User provided name: $user_login"
fi

#Считывание всех данных: пароля админа и временного пароля пользователя
while true; do
    read -p "Enter admin password: " adminPassword
    read -p "Enter temporary password: " userPassword
    read -p "Is everything correct? (y/n or just press Enter for yes): " -r
    if [[ $REPLY =~ ^([Yy][Ee][Ss]|[Yy])$ ]] || [[ -z $REPLY ]]; then
        echo "Input confirmed. Continuing..."
        break  
    else
        echo "Input incorrect. Please try again."
    fi
done

#Смена пароля и проверка смены
passchange=$(sysadminctl -secureTokenOn "$user_login" -password "$userPassword" -adminUser admin -adminPassword "$adminPassword" 2>&1)
if echo "$passchange" | grep -q "Done!"; then
    echo "Operation completed successfully with 'Done!'. Token is on. Password changed successfully"
else
    echo "Operation did not output 'Done!'. Exiting script, Token is off."
    echo "Output: $passchange"
    exit 1 #ВОТ ТУТ С АУТПУТОМ НАДО ПОСМОТРЕТЬ, ТОЧНО ЛИ ТАМ Done! ???
fi

#получение имена пакета с утилитой серта
cert=$(ls | grep .pkg)
path="${DIR// /\\ }"
#Создание скрипта для запуска из-под юзера
cat <<EOF > user.sh
#!/bin/bash
# Check Secure Token status for admin
admin_pass="${adminPassword}"
ad_login="${user_login}"
ad_temp_pass="${userPassword}"
echo -n "${userPassword}" | pbcopy

open $path/$cert
read -p "Is certificate installed? (y/n or just press Enter for yes): " -r

#Ручная проверка установки скрипта 
if [[ \$REPLY =~ ^([Yy][Ee][Ss]|[Yy])$ ]] || [[ -z \$REPLY ]]; then 
    echo "certficicate installed. Continuing..."
else
    echo "certificate uninstalled. Exiting..."
    exit 1
fi

# Отключение токена у админа
output=\$(sysadminctl -secureTokenOff admin -password "\$admin_pass" -adminUser "\$ad_login" -adminPassword "\$ad_temp_pass" 2>&1)
if echo "\$output" | grep -q "Done!"; then
    echo "Operation completed successfully with 'Done!'. Token checked succesfully"
else
    echo "Operation did not output 'Done!'. Exiting script token check operation."
    echo "Output: \$output"
    exit 1
fi

# Удаление админа из setup list
adminCheckOutput=\$(sudo fdesetup list)
if echo "\$adminCheckOutput" | grep -iq "admin"; then
    echo "Admin user found, removing using 'fdesetup remove'."
    sudo fdesetup remove -user admin
fi

while true; do
    status=\$(echo "${userPassword}" | sudo -S profiles status -type bootstraptoken)
    echo
    if echo "\$status" | grep -q "NO"; then
        echo "An issue has been detected with the Bootstrap Token status."
        echo "Please fix the issue (open macOS Healing Tool)"
        echo "press Enter to open Self Service"
        read -r
        open -a /Applications/Self\ Service.app
        echo "Press Enter to check again."
        read -r
        continue
    else
        echo "Bootstrap Token status is OK."
        break
    fi
done

# Самоудаление скрипта user.sh
script_path="\$( cd "\$( dirname "\${BASH_SOURCE[0]}" )" &> /dev/null && pwd )/\$(basename "\$0")"
if [ -f "\$script_path" ]; then
    rm -- "\$script_path"
else
    echo "Failed to delete the script: \$script_path"
fi

# Спрашиваем про перезагрузку
read -p "Do you want to reboot? (y/n) " -r

if [[ \$REPLY =~ ^([Yy][Ee][Ss]|[Yy])$ ]] || [[ -z \$REPLY ]]; then
    echo "Rebooting now."
    sudo shutdown -r now -t
fi
EOF
chmod +x user.sh

#разлогиниваемся из админа
osascript -e 'tell application "System Events" to log out'



# echo -n "${adminPassword}" | pbcopy 
# echo "The Admin password is in clipboard"
# Проверяем, есть ли пользователь в списке FileVault
# if ! fdesetup list | grep -q "^$ad_login,"; then
#   echo "User $ad_login is not found in FileVault list. Adding..."
#   echo "$adminPassword" | sudo -S fdesetup add -usertoadd $ad_login -password "$userPassword"
# else
#   echo "Пользователь $ad_login есть в списке FileVault."
# fi