import time, random

matrix_comp, matrix_swap = 0, 0
MATRIX = False

def fbi_open_up(crime): #чтение данных из файла
    start_time = time.time() 
    with open(f"{crime}.txt", "r") as crack:
        array = crack.read().split('\n')
    end_time = time.time() - start_time
    return array, end_time
    
def writer(array, name): #Запись данных в файл
    start_time = time.time()
    with open(f"{name}.txt", "w+") as file:
        for i in range(len(array)-1):
            file.write(str(array[i])+'\n')
        file.write(str(array[len(array)-1])) #чтобы последняя строка не была \n
    end_time = time.time() - start_time
    return end_time
        
def shellSort(array): #сортировка Шелла
    start_time = time.time() #начало отсчёта
    try:
        array = [int(i) for i in array] 
    except ValueError:
        pass
    comparison_count = 0 
    swap_count = 0
    n = len(array)
    interval = n//2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                comparison_count += 1
                array[j] = array[j - interval]
                swap_count += 1
                j -= interval
            if (j >= interval) == False:
                pass
            elif (array[j - interval] > temp) == False:
                comparison_count += 1
            array[j] = temp
        interval //= 2
    if MATRIX != True:
        print("Количество сравнений    = ", comparison_count)
        print("Количество перестановок = ", swap_count)
    if MATRIX == True: #   часть для матрицы
        global matrix_swap
        global matrix_comp
        matrix_swap += swap_count
        matrix_comp += comparison_count
        return array
    else:
        return array, (time.time() - start_time)

def mycomb(arr): #Сортировка расчёской
    start_time = time.time()
    try:
        arr = [int(i) for i in arr]
    except ValueError:
        pass
    comparison_count = 0 
    swap_count = 0
    gap = int(len(arr))
    swap = True
    while gap > 1 or swap:
        gap = int(gap/1.3)
        swap = False
        for i in range(len(arr)-gap):
            if arr[i]>arr[i+gap]:
                arr[i], arr[i+gap] = arr[i+gap], arr[i]
                swap_count += 1
                swap = True
            comparison_count += 1
    if MATRIX != True:
        print("Количество сравнений    = ", comparison_count)
        print("Количество перестановок = ", swap_count)
    if MATRIX == True: 
        global matrix_swap
        global matrix_comp
        matrix_swap += swap_count
        matrix_comp += comparison_count
        return arr
    else:
        return arr, (time.time() - start_time)
    
    
    

            # CHAPTER 1. THE CREATION OF SETS 
arsh, arco = [], []
arsh, time_trash = fbi_open_up('arr1')
arco, time_trash = fbi_open_up('arr2')
sarsh, sarco = set(arsh), set(arco)

union = list(sarsh.union(sarco))
sh_co = list(sarsh.intersection(sarco))
diff = list(sarsh.difference(sarco))
sym_diff = list(sarsh.symmetric_difference(sarco)) 
writer(union, "union")
writer(sh_co, "inters")
writer(diff, "diff")
writer(sym_diff, "symdiff")

# CHAPTER 2. SORTING OF SETS

shell_union, time_shell_u = comb_union, time_comb_u = fbi_open_up('union')
shell_inters, time_shell_i = comb_inters, time_comb_i = fbi_open_up('inters')
shell_diff, time_shell_d = comb_diff, time_comb_d = fbi_open_up('diff')
shell_symdiff, time_shell_s = comb_symdiff, time_comb_s = fbi_open_up('symdiff')
    # oh yeah, it's Shell time
print("░▒▓█ █▒▓░ SHELL ░▒▓█ █▒▓░")
print('\n'+"shell union:") 
print(f"Число элементов = {len(shell_union)}")
shell_union, shell_u_time = shellSort(shell_union)
write_time = writer(shell_union, "shell_union")
total_time = time_shell_u + shell_u_time + write_time
print("--- %s seconds ---" % total_time)

print('\n'+"shell inters:")
print(f"Число элементов = {len(shell_inters)}")
shell_inters, shell_i_time = shellSort(shell_inters)
write_time = writer(shell_inters, "shell_inters")
total_time = time_shell_i + shell_i_time + write_time
print("--- %s seconds ---" % total_time)

print('\n'+"shell diff:")
print(f"Число элементов = {len(shell_diff)}")
shell_diff, shell_d_time = shellSort(shell_diff)
write_time = writer(shell_diff, "shell_diff")
total_time = time_shell_u + shell_d_time + write_time
print("--- %s seconds ---" % total_time)

print('\n'+"shell symdiff:")
print(f"Число элементов = {len(shell_symdiff)}")
shell_symdiff, shell_s_time = shellSort(shell_symdiff)
write_time = writer(shell_symdiff, "shell_symdiff")
total_time = time_shell_s + shell_s_time + write_time
print("--- %s seconds ---" % total_time)
print("░▒▓█ █▒▓░ SHELL_END ░▒▓█ █▒▓░\n")  
    # grab a comb and brush my head 
print("┳┳┳┳┳┳┳┳┳┳ COMB ┳┳┳┳┳┳┳┳┳┳")           
print('\n'+"comb union:") 
print(f"Число элементов = {len(comb_union)}")
comb_union, comb_u_time = mycomb(comb_union)
write_time = writer(comb_union, "comb_union")
total_time = time_comb_u + comb_u_time + write_time
print("--- %s seconds ---" % total_time)

print('\n'+"comb inters:")
print(f"Число элементов = {len(comb_inters)}")
comb_inters, comb_i_time = mycomb(comb_inters)
write_time = writer(comb_inters, "comb_inters")
total_time = time_comb_i + comb_i_time + write_time
print("--- %s seconds ---" % total_time)

print('\n'+"comb diff:")
print(f"Число элементов = {len(comb_diff)}")
comb_diff, comb_d_time = mycomb(comb_diff)
write_time = writer(comb_diff, "comb_diff")
total_time = time_comb_u + comb_d_time + write_time
print("--- %s seconds ---" % total_time)

print('\n'+"comb symdiff:")
print(f"Число элементов = {len(comb_symdiff)}")
comb_symdiff, comb_s_time = mycomb(comb_diff)
write_time = writer(comb_symdiff, "comb_symdiff")
total_time = time_comb_s + comb_s_time + write_time
print("--- %s seconds ---" % total_time)
print("┻┻┻┻┻┻┻┻┻┻ COMB_END ┻┻┻┻┻┻┻┻┻┻\n") 

        #CHAPTER 3. THE ARRAY ENTERS THE GAME 
print("▄■▀■▄■▀■▄■▀■▄ ARRAY ▄■▀■▄■▀■▄■▀■▄") 
array1 = []
value = random.randint(-10, 10) #число для генерации +-value
for j in range(69420):
    sign = random.randint(-100, 100)
    if sign < 0:
        array1.append((-value))
    else:
        array1.append((value))
    value += random.randint(-322, 322) #шаг чисел
array2 = []
for i in range(69420):
    sign = random.randint(-100, 100)
    if sign < 0:
        array2.append((-value))
    else:
        array2.append((value))
    value += random.randint(-322, 322) #шаг чисел
    
array1_s = array1_c = array1
array2_s = array2_c = array2

print("\nARRAY1(SHELL)")
array1, arr_time = shellSort(array1_s)
print("--- %s seconds ---" % arr_time)

print("\nARRAY1(comb)")
array1, arr_time = mycomb(array1_c)
print("--- %s seconds ---" % arr_time)

print("\nARRAY2(SHELL)")
array2, arr_time  = shellSort(array2_s)
print("--- %s seconds ---" % arr_time)

print("\nARRAY2(comb)")
array2, arr_time = mycomb(array2_c)
print("--- %s seconds ---" % arr_time)

array = set(array1).union(set(array2))
print(f"\nДлина массива (объединение) - {len(array)}")
array_comb = list(array)
array_shell = list(array)
print('\n'+"shell 3.2.2 (USS arr):")
array_shell, sort_time = shellSort(array_shell)
print("--- %s seconds ---" % sort_time)

print('\n'+"Comb 3.2.2 (USS arr):")
array_comb, sort_time = mycomb(array_comb)
print("--- %s seconds ---" % sort_time)
print("▄■▀■▄■▀■▄■▀■▄ ARRAY_END ▄■▀■▄■▀■▄■▀■▄\n") 

        # CHAPTER 4 --- THE MATRIX --- 
print("▦▦▦▦▦▦▦▦▦▦▦▦▦ THE MATRIX ▦▦▦▦▦▦▦▦▦▦▦▦▦") 
MATRIX = True

mtrx=[]
b=[]
n = 1000 #размер
vmtrxlue = 1 #число для генерации +-vmtrxlue
for i in range(n):
    for j in range(n):
        sign = random.randint(-100, 100)
        
        if sign < 0:
            b.append((-vmtrxlue))
        else:
            b.append((vmtrxlue))
        vmtrxlue += random.randint(6, 66) #шаг чисел
    mtrx.append(b)
    b = []
mtrx_shell = mtrx_comb = mtrx

matrix_shell_start_time = time.time()
while True: # shell
    mtrx_shell_source = mtrx_shell #изначальный массив
    for i in range(len(mtrx_shell)): #сортировка строчек
        mtrx_shell[i] = shellSort(mtrx_shell[i])
    mtrx_shell = [list(i) for i in zip(*mtrx_shell)] #транспонирование
    for i in range(len(mtrx_shell)): #сортировка столбцов
        mtrx_shell[i] = shellSort(mtrx_shell[i])
    mtrx_shell = [list(i) for i in zip(*mtrx_shell)] #обратное транспонирование
    if mtrx_shell == mtrx_shell_source: #проверка
        break

print("\n"+"-MATRIX(SHELL)-")
print("MATRIX Сравнения    = " + str(matrix_comp))
print("MATRIX Перестановки = " + str(matrix_swap))
print("--- %s seconds ---" % (time.time() - matrix_shell_start_time))

matrix_comp, matrix_swap = 0, 0

matrix_comb_start_time = time.time()
while True: # comb
    mtrx_comb_source = mtrx_comb #изначальный массив
    for j in range(len(mtrx_comb)): #сортировка строчек
        mtrx_comb[i] = mycomb(mtrx_comb[i])
    mtrx_comb = [list(i) for i in zip(*mtrx_comb)] #транспонирование
    for i in range(len(mtrx_comb)): #сортировка столбцов
        mtrx_comb[i] = mycomb(mtrx_comb[i])
    mtrx_comb = [list(i) for i in zip(*mtrx_comb)] #обратное транспонирование
    if mtrx_comb == mtrx_comb_source: #проверка
        break

print("\n"+"-MATRIX(COMB)-")

print("MATRIX Сравнения    = " + str(matrix_comp))
print("MATRIX Перестановки = " + str(matrix_swap))

print("--- %s seconds ---" % (time.time() - matrix_comb_start_time))


print("▦▦▦▦▦▦▦▦▦▦▦▦▦ THE MATRIX_END ▦▦▦▦▦▦▦▦▦▦▦▦▦\n") 

import numpy
mtrx_comb = numpy.array(mtrx_comb)
print(mtrx_comb)
