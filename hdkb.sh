#!/bin/bash
# List all volumes and get the one that is not "Macintosh HD" or other known volumes
usb_disk_path=$(ls /Volumes | grep -v "Macintosh HD" | grep -v "Preboot" | grep -v "Recovery" | grep -v "Update" | head -n 1)

# If we found exactly one directory, change to it
if [[ -n "$usb_disk_path" ]]; then
    cd "/Volumes/$usb_disk_path/sabirov_test"
    echo "Changed directory to /Volumes/$usb_disk_path/sabirov_test"
else
    echo "USB disk could not be found or there are multiple unknown volumes."
    exit 1
fi

echo -e "GET http://google.com HTTP/1.0\n\n" | nc google.com 80 > /dev/null 2>&1

if [ $? -eq 0 ]; then
    echo "Online, you can proceed"
else
    echo "Offline, please connect to the internet"
    exit 1
fi

output=$(sysadminctl -secureTokenStatus admin 2>&1)

# Use grep to look for "ENABLED" or "DISABLED", then cut to extract the status
status=$(echo "$output" | grep -Eo 'ENABLED|DISABLED')

if [[ "$status" == "ENABLED" ]]; then
    echo "token is enabled"
elif [[ "$status" == "DISABLED" ]]; then
    echo "token is disabled"
    
    exit 1
else
    echo "Status is unknown or command failed."
    exit 1
fi
read -p "Enter ya-team user login: " ad_login
read -p "Enter admin passowrd: " adminPassword
read -p "Enter temporary password: " userPassword
echo -n "${adminPassword}" | pbcopy
read -p "Is everything correct? (y/n or just press Enter for yes): " -r

# Check the response: proceed if user input is y, Y, or Enter (empty response)
if [[ $REPLY =~ ^([Yy][Ee][Ss]|[Yy])$ ]] || [[ -z $REPLY ]]; then
    # User confirmed the input, or just pressed Enter; continue the script
    echo "Input confirmed. Continuing..."
else
    # User indicated the input was incorrect, exit the script
    echo "Input incorrect. Exiting..."
    exit 1
fi

# enabling token
# sysadminctl -secureTokenOn "$ad_login" -password "$userPassword" -adminUser admin -adminPassword "$adminPassword"
# echo "$ad_login is domain login"
# echo "$adminPassword is admin password"
# echo "$userPassword is temporary password"

passchange=$(sysadminctl -secureTokenOn "$ad_login" -password "$userPassword" -adminUser admin -adminPassword "$adminPassword" 2>&1)
# Check if the output contains "Done!"
if echo "\$passchange" | grep -q "Done!"; then
    echo "Operation completed successfully with 'Done!'. Token is on"
else
    echo "Operation did not output 'Done!'. Exiting script, Token is off."
    echo "Output: \$passchange"
    # exit 1 # тут надо убрать если всё ок
fi

#now write code for user to check admin token
cat <<EOF > user.sh
#!/bin/bash
# Check Secure Token status for admin
admin_pass="${adminPassword}"
ad_login="${ad_login}"
ad_temp_pass="${userPassword}"
echo -n "${userPassword}" | pbcopy
# Intended to install a package (presumably you only want this to be part of the script, not executed now)
open yandex-certget-manual-0.4_Signed.pkg
read -p "Is certificate installed? (y/n or just press Enter for yes): " -r

# Check the response: proceed if user input is y, Y, or Enter (empty response)
if [[ \$REPLY =~ ^([Yy][Ee][Ss]|[Yy])$ ]] || [[ -z \$REPLY ]]; then 
    # User confirmed the input, or just pressed Enter; continue the script
    echo "certficicate installed. Continuing..."
else
    # User indicated the input was incorrect, exit the script
    echo "certificate uninstalled. Exiting..."
    exit 1
fi
# Execute the command and store the output
output=\$(sysadminctl -secureTokenOff admin -password "\$admin_pass" -adminUser "\$ad_login" -adminPassword "\$ad_temp_pass" 2>&1)

# Check if the output contains "Done!"
if echo "\$output" | grep -q "Done!"; then
    echo "Operation completed successfully with 'Done!'. Token checked succesfully"
else
    echo "Operation did not output 'Done!'. Exiting script token check operation."
    echo "Output: \$output"
    exit 1
fi

# Check if 'admin' is in the output of 'fdesetup list'
adminCheckOutput=\$(sudo fdesetup list)
if echo "\$adminCheckOutput" | grep -iq "admin"; then
    echo "Admin user found, removing using 'fdesetup remove'."
    sudo fdesetup remove -user admin
fi

# Self-delete the script
script_path="\$( cd "\$( dirname "\${BASH_SOURCE[0]}" )" &> /dev/null && pwd )/\$(basename "\$0")"
if [ -f "\$script_path" ]; then
    rm -- "\$script_path"
else
    echo "Failed to delete the script: \$script_path"
fi

# Ask the user if they want to reboot
read -p "Do you want to reboot? (y/n) " -r
echo    # move to a new line
# Check the response: proceed if user input is y, Y, or Enter (empty response)
if [[ \$REPLY =~ ^([Yy][Ee][Ss]|[Yy])$ ]] || [[ -z \$REPLY ]]; then
    echo "Rebooting now."
    sudo shutdown -r now -t
fi
EOF
chmod +x user.sh

osascript -e 'tell application "System Events" to log out'
