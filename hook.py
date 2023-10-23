import time
import random 

matrix_comp, matrix_swap = 0, 0

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
            comparison_count += 1
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                swap_count += 1
                j -= interval
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
    return array

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
            comparison_count += 1
            if arr[i]>arr[i+gap]:
                swap_count += 1
                arr[i], arr[i+gap] = arr[i+gap], arr[i]
                swap = True
    if MATRIX == True:
        matrix_swap += swap_count
        matrix_comp += comparison_count
    if MATRIX != True:
        print("--- %s seconds ---" % (time.time() - start_time))
        print("comparisons = ", comparison_count)
        print("swaps = ", swap_count)
    return arr


arsh, arco = [], []

            # CHAPTER 1. THE CREATION OF SETS 
MATRIX = False

with open("arr1.txt", "r") as shell, open("arr2.txt", "r") as comb:
    arsh, arco = shell.read().split('\n'), comb.read().split('\n')
    sarsh, sarco = set(arsh), set(arco)
    
    union = list(sarsh.union(sarco))
    sh_co = list(sarsh.intersection(sarco))
    diff = list(sarsh.difference(sarco))
    sym_diff = list(sarsh.symmetric_difference(sarco))
    
    with open("union.txt", "w+") as f_union, open("inters.txt", "w+") as f_inters, open("diff.txt", "w+") as f_diff, open("symdiff.txt", "w+") as f_symdiff:
        for i in range(len(union)):
            if i == len(union)-1:
                f_union.write(str(union[i]))
            else:
                f_union.write(str(union[i])+'\n')
        for i in range(len(sh_co)):
            if i == len(sh_co)-1:
                f_inters.write(str(sh_co[i]))
            else:
                f_inters.write(str(sh_co[i])+'\n')
        for i in range(len(diff)):
            if i == len(diff)-1:
                f_diff.write(str(diff[i]))
            else:
                f_diff.write(str(diff[i])+'\n')
        for i in range(len(sym_diff)):
            if i == len(sym_diff)-1:
                f_symdiff.write(str(sym_diff[i]))
            else:
                f_symdiff.write(str(sym_diff[i])+'\n')

# CHAPTER 2. SORTING OF SETS

with open("union.txt", "r") as f_union, open("inters.txt", "r") as f_inters, open("diff.txt", "r") as f_diff, open("symdiff.txt", "r") as f_symdiff:
    union, inters, diff, sym_diff = f_union.read().split('\n'), f_inters.read().split('\n'), f_diff.read().split('\n'), f_symdiff.read().split('\n')
    
    shell_union, comb_union = union, union
    shell_inters, comb_inters = inters, inters
    shell_diff, comb_diff =  diff, diff
    shell_symdiff, comb_symdiff = sym_diff, sym_diff
    
    # oh yeah, it's Shell time
    print("____________________SHELL____________________")
    print('\n'+"shell union:")
    shell_union = shellSort(shell_union)
    print('\n'+"shell inters:")
    shell_inters = shellSort(shell_inters)
    print('\n'+"shell diff:")
    shell_diff = shellSort(shell_diff)
    print('\n'+"shell symdiff:")
    shell_symdiff = shellSort(shell_symdiff)
    
    with open("shell_union.txt", "w+") as fshell_union, open("shell_inters.txt", "w+") as fshell_inters, open("shell_diff.txt", "w+") as fshell_diff, open("shell_symdiff.txt", "w+") as fshell_symdiff:
        for i in range(len(shell_union)):
            if i == len(shell_union)-1:
                fshell_union.write(str(shell_union[i]))
            else:
                fshell_union.write(str(shell_union[i])+'\n')
        for i in range(len(shell_inters)):
            if i == len(shell_inters)-1:
                fshell_inters.write(str(shell_inters[i]))
            else:
                fshell_inters.write(str(shell_inters[i])+'\n')
        for i in range(len(shell_diff)):
            if i == len(shell_diff)-1:
                fshell_diff.write(str(shell_diff[i]))
            else:
                fshell_diff.write(str(shell_diff[i])+'\n')
        for i in range(len(shell_symdiff)):
            if i == len(shell_symdiff)-1:
                fshell_symdiff.write(str(shell_symdiff[i]))
            else:
                fshell_symdiff.write(str(shell_symdiff[i])+'\n')
    print("____________________SHELL_END____________________\n")
    
    # grab a comb and brush my head 
    print("____________________COMB____________________")           
    print('\n'+"comb union:")
    comb_union = mycomb(comb_union)
    print('\n'+"comb inters:")
    comb_inters = mycomb(comb_inters)
    print('\n'+"comb diff:")
    comb_diff = mycomb(comb_diff)
    print('\n'+"comb symdiff:")
    comb_symdiff = mycomb(comb_symdiff)
    print("____________________COMB_END____________________\n") 
    with open("comb_union.txt", "w+") as fcomb_union, open("comb_inters.txt", "w+") as fcomb_inters, open("comb_diff.txt", "w+") as fcomb_diff, open("comb_symdiff.txt", "w+") as fcomb_symdiff:
        for i in range(len(comb_union)):
            if i == len(comb_union)-1:
                fcomb_union.write(str(comb_union[i]))
            else:
                fcomb_union.write(str(comb_union[i])+'\n')
        for i in range(len(comb_inters)):
            if i == len(comb_inters)-1:
                fcomb_inters.write(str(comb_inters[i]))
            else:
                fcomb_inters.write(str(comb_inters[i])+'\n')
        for i in range(len(comb_diff)):
            if i == len(comb_diff)-1:
                fcomb_diff.write(str(comb_diff[i]))
            else:
                fcomb_diff.write(str(comb_diff[i])+'\n')
        for i in range(len(comb_symdiff)):
            if i == len(comb_symdiff)-1:
                fcomb_symdiff.write(str(comb_symdiff[i]))
            else:
                fcomb_symdiff.write(str(comb_symdiff[i])+'\n')

        #CHAPTER 3. THE ARRAY ENTERS THE GAME 
print("____________________ARRAY____________________") 
array1 = []
value = random.randint(-10, 10) #число для генерации +-value
for j in range(2501):
    sign = random.randint(-100, 100)
    if sign < 0:
        array1.append((-value))
    else:
        array1.append((value))
    value += random.randint(-50, 50) #шаг чисел
array2 = []
for i in range(2501):
    sign = random.randint(-100, 100)
    if sign < 0:
        array2.append((-value))
    else:
        array2.append((value))
    value += random.randint(-50, 50) #шаг чисел
print("\nARRAY1(SHELL)")
array1 = shellSort(array1)
print("\nARRAY2(COMB)")
array2 = mycomb(array2)

array = set(array1).union(set(array2))
array_comb = list(array)
array_shell = list(array)
print('\n'+"shell 3.2.2:")
shellSort(array_shell)
print('\n'+"Comb 3.2.2:")
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
        value += random.randint(-50, 50) #шаг чисел
    a.append(b)
    b = []
a_shell, a_comb = a, a

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

matrix_comb_start_time = time.time()
while True: # comb
    a_comb_source = a_comb #изначальный массив
    for i in range(len(a_comb)): #сортировка строчек
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

# print('\n-----SORTED MATRIX GO BRRR-----\n')
# for i in a:
#     print(i)
print("____________________THE MATRIX_END____________________") 
