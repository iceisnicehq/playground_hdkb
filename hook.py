import time
import random 

matrix_comp, matrix_swap = 0, 0

def fbi_open_up(crime):
    start_time = time.time()
    with open(f"{crime}.txt", "r") as crack:
        array = crack.read().split('\n')
    end_time = time.time() - start_time
    return array, end_time
    
    
def writer(array, name):
    start_time = time.time()
    with open(f"{name}.txt", "w+") as file:
        for i in range(len(array)):
                if i == len(array)-1:
                    file.write(str(array[i]))
                else:
                    file.write(str(array[i])+'\n')
    end_time = time.time() - start_time
    return end_time
        
def shellSort(array): #сортировка Шелла
    global matrix_swap # для матрицы
    global matrix_comp
    try:
        array = [int(i) for i in array] 
    except ValueError:
        pass
    start_time = time.time() #начало отсчёта
    comparison_count = 0 
    swap_count = 0
    n = len(array)
    k = n//2
    interval = 2**k -1
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                comparison_count += 1
                array[j] = array[j - interval]
                swap_count += 1
                j -= interval
            if (array[j - interval] > temp) == False:
                comparison_count += 1
            array[j] = temp
            # swap_count += 1
        k -= 1
        interval = 2**k -1
    if MATRIX == True:
        matrix_swap += swap_count
        matrix_comp += comparison_count
    if MATRIX != True:
        print("--- %s seconds ---" % (time.time() - start_time))
        print("comparisons = ", comparison_count)
        print("swaps = ", swap_count)
    if MATRIX == True:
        return array
    else:
        return array, (time.time() - start_time)

def mycomb(arr):
    global matrix_swap
    global matrix_comp
    try:
        arr = [int(i) for i in arr]
    except ValueError:
        pass
    start_time = time.time()
    comparison_count = 0 
    swap_count = 0
    gap = int(len(arr))
    swap = True

    while gap > 1 or swap:
        gap = int(gap/1.3)
        swap = False
        for i in range(len(arr)-gap):
            
            if arr[i]>arr[i+gap]:
                comparison_count += 1
                arr[i], arr[i+gap] = arr[i+gap], arr[i]
                swap_count += 1
                swap = True
            if (arr[i]>arr[i+gap]) == False:
                comparison_count += 1
    if MATRIX == True:
        matrix_swap += swap_count
        matrix_comp += comparison_count
    if MATRIX != True:
        print("--- %s seconds ---" % (time.time() - start_time))
        print("comparisons = ", comparison_count)
        print("swaps = ", swap_count)
    if MATRIX == True:
        return arr
    elif MATRIX != True:
        return arr, (time.time() - start_time)


arsh, arco = [], []

            # CHAPTER 1. THE CREATION OF SETS 
MATRIX = False

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
print("____________________SHELL____________________")
print('\n'+"shell union:")
shell_union, shell_u_time = shellSort(shell_union)
write_time = writer(shell_union, "shell_union")
total_time = time_shell_u + shell_u_time + write_time
print("--- %s seconds ---" % total_time)

print('\n'+"shell inters:")
shell_inters, shell_i_time = shellSort(shell_inters)
write_time = writer(shell_inters, "shell_inters")
total_time = time_shell_i + shell_i_time + write_time
print("--- %s seconds ---" % total_time)

print('\n'+"shell diff:")
shell_diff, shell_d_time = shellSort(shell_diff)
write_time = writer(shell_diff, "shell_diff")
total_time = time_shell_u + shell_d_time + write_time
print("--- %s seconds ---" % total_time)

print('\n'+"shell symdiff:")
shell_symdiff, shell_s_time = shellSort(shell_diff)
write_time = writer(shell_symdiff, "shell_symdiff")
total_time = time_shell_s + shell_s_time + write_time
print("--- %s seconds ---" % total_time)

    # grab a comb and brush my head 
print("____________________COMB____________________")           
print('\n'+"comb union:") 
comb_union, comb_u_time = mycomb(comb_union)
write_time = writer(comb_union, "comb_union")
total_time = time_comb_u + comb_u_time + write_time
print("--- %s seconds ---" % total_time)

print('\n'+"comb inters:")
comb_inters, comb_i_time = mycomb(comb_inters)
write_time = writer(comb_inters, "comb_inters")
total_time = time_comb_i + comb_i_time + write_time
print("--- %s seconds ---" % total_time)

print('\n'+"comb diff:")
comb_diff, comb_d_time = mycomb(comb_diff)
write_time = writer(comb_diff, "comb_diff")
total_time = time_comb_u + comb_d_time + write_time
print("--- %s seconds ---" % total_time)

print('\n'+"comb symdiff:")
comb_symdiff, comb_s_time = mycomb(comb_diff)
write_time = writer(comb_symdiff, "comb_symdiff")
total_time = time_comb_s + comb_s_time + write_time
print("--- %s seconds ---" % total_time)

print("____________________COMB_END____________________\n") 

print("____________________ARRAY____________________") 
array1 = []
value = random.randint(-10, 10) #число для генерации +-value
for j in range(6969):
    sign = random.randint(-100, 100)
    if sign < 0:
        array1.append((-value))
    else:
        array1.append((value))
    value += random.randint(-50, 50) #шаг чисел
array2 = []
for i in range(6660):
    sign = random.randint(-100, 100)
    if sign < 0:
        array2.append((-value))
    else:
        array2.append((value))
    value += random.randint(-50, 50) #шаг чисел
print("\nARRAY1(SHELL)")
array1, trash_time = shellSort(array1)
print("\nARRAY2(COMB)")
array2, trash_time = mycomb(array2)

array = set(array1).union(set(array2))
array_comb = list(array)
array_shell = list(array)
print('\n'+"shell 3.2.2 (USS arr):")
shellSort(array_shell)
print('\n'+"Comb 3.2.2 (USS arr):")
mycomb(array_comb)
print("____________________ARRAY_END____________________\n") 

        # CHAPTER 4 --- THE MATRIX --- 
print("____________________THE MATRIX____________________") 
MATRIX = True

a=[]
b=[]
n = 1000 #размер
value = 1 #число для генерации +-value
for i in range(n):
    for j in range(n):
        sign = random.randint(-100, 100)
        
        if sign < 0:
            b.append((-value))
        else:
            b.append((value))
        value += random.randint(6, 66) #шаг чисел
    a.append(b)
    b = []
a_shell = a_comb = a

matrix_shell_start_time = time.time()
while True: # shell
    a_shell_source = a_shell #изначальный массив
    for i in range(len(a_shell)): #сортировка строчек
        a_shell[i] = shellSort(a_shell[i])
    a_shell = [list(i) for i in zip(*a_shell)] #транспонирование
    for i in range(len(a_shell)): #сортировка столбцов
        a_shell[i] = shellSort(a_shell[i])
    a_shell = [list(i) for i in zip(*a_shell)] #обратное транспонирование
    if a_shell == a_shell_source: #проверка
        break
print("\n"+"-MATRIX(SHELL)-- %s seconds ---" % (time.time() - matrix_shell_start_time))
print("MATRIX SWAPS " + str(matrix_swap))
print("MATRIX COMPS " + str(matrix_comp))

matrix_comp, matrix_swap = 0, 0

matrix_comb_start_time = time.time()
while True: # comb
    a_comb_source = a_comb #изначальный массив
    for j in range(len(a_comb)): #сортировка строчек
        a_comb[i] = mycomb(a_comb[i])
    a_comb = [list(i) for i in zip(*a_comb)] #транспонирование
    for i in range(len(a_comb)): #сортировка столбцов
        a_comb[i] = mycomb(a_comb[i])
    a_comb = [list(i) for i in zip(*a_comb)] #обратное транспонирование
    if a_comb == a_comb_source: #проверка
        break

print("\n"+"-MATRIX(COMB)-- %s seconds ---" % (time.time() - matrix_comb_start_time))
print("MATRIX SWAPS " + str(matrix_swap))
print("MATRIX COMPS " + str(matrix_comp))
print("____________________THE MATRIX_END____________________") 
