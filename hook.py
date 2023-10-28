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
    start_time = time.time() #начало отсчёта
    try:
        array = [int(i) for i in array] 
    except ValueError:
        pass
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
            if (j >= interval) == False:
                pass
            elif (array[j - interval] > temp) == False:
                comparison_count += 1
            array[j] = temp
            # swap_count += 1
        k -= 1
        interval = 2**k -1
    if MATRIX != True:
        print("--- %s seconds ---" % (time.time() - start_time))
        print("comparisons = ", comparison_count)
        print("swaps = ", swap_count)
    if MATRIX == True:
        global matrix_swap
        global matrix_comp
        matrix_swap += swap_count
        matrix_comp += comparison_count
        return array
    else:
        return array, (time.time() - start_time)

def mycomb(arr):
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
        print("--- %s seconds ---" % (time.time() - start_time))
        print("comparisons = ", comparison_count)
        print("swaps = ", swap_count)
    if MATRIX == True:
        global matrix_swap
        global matrix_comp
        matrix_swap += swap_count
        matrix_comp += comparison_count
        return arr
    elif MATRIX != True:
        return arr, (time.time() - start_time)


arsh, arco = [], []

            # CHAPTER 1. THE CREATION OF SETS 
MATRIX = False

arsh, time_trash = fbi_open_up('arr1')
arco, time_trash = fbi_open_up('arr2')
sarsh, sarco = set(arsh), set(arco)
# with open("arr1.txt", "r") as shell, open("arr2.txt", "r") as comb:
#     arsh, arco = shell.read().split('\n'), comb.read().split('\n')
#     sarsh, sarco = set(arsh), set(arco)

union = list(sarsh.union(sarco))
sh_co = list(sarsh.intersection(sarco))
diff = list(sarsh.difference(sarco))
sym_diff = list(sarsh.symmetric_difference(sarco)) 
writer(union, "union")
writer(sh_co, "inters")
writer(diff, "diff")
writer(sym_diff, "symdiff")
# with open("union.txt", "w+") as f_union, open("inters.txt", "w+") as f_inters, open("diff.txt", "w+") as f_diff, open("symdiff.txt", "w+") as f_symdiff:
#     for i in range(len(union)):
#         if i == len(union)-1:
#             f_union.write(str(union[i]))
#         else:
#             f_union.write(str(union[i])+'\n')
#     for i in range(len(sh_co)):
#         if i == len(sh_co)-1:
#             f_inters.write(str(sh_co[i]))
#         else:
#             f_inters.write(str(sh_co[i])+'\n')
#     for i in range(len(diff)):
#         if i == len(diff)-1:
#             f_diff.write(str(diff[i]))
#         else:
#             f_diff.write(str(diff[i])+'\n')
#     for i in range(len(sym_diff)):
#         if i == len(sym_diff)-1:
#             f_symdiff.write(str(sym_diff[i]))
#         else:
#             f_symdiff.write(str(sym_diff[i])+'\n')

# CHAPTER 2. SORTING OF SETS

shell_union, time_shell_u = comb_union, time_comb_u = fbi_open_up('union')
shell_inters, time_shell_i = comb_inters, time_comb_i = fbi_open_up('inters')
shell_diff, time_shell_d = comb_diff, time_comb_d = fbi_open_up('diff')
shell_symdiff, time_shell_s = comb_symdiff, time_comb_s = fbi_open_up('symdiff')
# with open("union.txt", "r") as f_union, open("inters.txt", "r") as f_inters, open("diff.txt", "r") as f_diff, open("symdiff.txt", "r") as f_symdiff:
#     union, inters, diff, sym_diff = f_union.read().split('\n'), f_inters.read().split('\n'), f_diff.read().split('\n'), f_symdiff.read().split('\n')
    
#     shell_union = comb_union = union
#     shell_inters = comb_inters = inters
#     shell_diff = comb_diff =  diff
#     shell_symdiff = comb_symdiff = sym_diff
    
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
shell_symdiff, shell_s_time = shellSort(shell_symdiff)
write_time = writer(shell_symdiff, "shell_symdiff")
total_time = time_shell_s + shell_s_time + write_time
print("--- %s seconds ---" % total_time)

'''

    shell_inters = shellSort(shell_inters)

    shell_diff = shellSort(shell_diff)
    
    shell_symdiff = shellSort(shell_symdiff)
    

    writer(shell_union, "shell_union")
    writer(shell_inters, "shell_inters")
    writer(shell_diff, "shell_diff")

    # with open("shell_union.txt", "w+") as fshell_union, open("shell_inters.txt", "w+") as fshell_inters, open("shell_diff.txt", "w+") as fshell_diff, open("shell_symdiff.txt", "w+") as fshell_symdiff:
    #     for i in range(len(shell_union)):
    #         if i == len(shell_union)-1:
    #             fshell_union.write(str(shell_union[i]))
    #         else:
    #             fshell_union.write(str(shell_union[i])+'\n')
    #     for i in range(len(shell_inters)):
    #         if i == len(shell_inters)-1:
    #             fshell_inters.write(str(shell_inters[i]))
    #         else:
    #             fshell_inters.write(str(shell_inters[i])+'\n')
    #     for i in range(len(shell_diff)):
    #         if i == len(shell_diff)-1:
    #             fshell_diff.write(str(shell_diff[i]))
    #         else:
    #             fshell_diff.write(str(shell_diff[i])+'\n')
    #     for i in range(len(shell_symdiff)):
    #         if i == len(shell_symdiff)-1:
    #             fshell_symdiff.write(str(shell_symdiff[i]))
    #         else:
    #             fshell_symdiff.write(str(shell_symdiff[i])+'\n')

print("____________________SHELL_END____________________\n")
'''    
    # grab a comb and brush my head 
print("____________________COMB____________________")           
print('\n'+"comb union:") 
comb_union, comb_u_time = mycomb(comb_union)
write_time = writer(comb_union, "comb_union")
total_time = time_comb_u + comb_u_time + write_time
print("--- %s seconds ---" % total_time)
# comb_union = mycomb(comb_union)
print('\n'+"comb inters:")
comb_inters, comb_i_time = mycomb(comb_inters)
write_time = writer(comb_inters, "comb_inters")
total_time = time_comb_i + comb_i_time + write_time
print("--- %s seconds ---" % total_time)

# comb_inters = mycomb(comb_inters)
print('\n'+"comb diff:")
comb_diff, comb_d_time = mycomb(comb_diff)
write_time = writer(comb_diff, "comb_diff")
total_time = time_comb_u + comb_d_time + write_time
print("--- %s seconds ---" % total_time)
# comb_diff = mycomb(comb_diff)
print('\n'+"comb symdiff:")
comb_symdiff, comb_s_time = mycomb(comb_diff)
write_time = writer(comb_symdiff, "comb_symdiff")
total_time = time_comb_s + comb_s_time + write_time
print("--- %s seconds ---" % total_time)
# comb_symdiff = mycomb(comb_symdiff)

# writer(comb_union, "comb_union")
# writer(comb_inters, "comb_inters")
# writer(comb_diff, "comb_diff")
# writer(comb_symdiff, "comb_symdiff")

print("____________________COMB_END____________________\n") 
# with open("comb_union.txt", "w+") as fcomb_union, open("comb_inters.txt", "w+") as fcomb_inters, open("comb_diff.txt", "w+") as fcomb_diff, open("comb_symdiff.txt", "w+") as fcomb_symdiff:
#     for i in range(len(comb_union)):
#         if i == len(comb_union)-1:
#             fcomb_union.write(str(comb_union[i]))
#         else:
#             fcomb_union.write(str(comb_union[i])+'\n')
#     for i in range(len(comb_inters)):
#         if i == len(comb_inters)-1:
#             fcomb_inters.write(str(comb_inters[i]))
#         else:
#             fcomb_inters.write(str(comb_inters[i])+'\n')
#     for i in range(len(comb_diff)):
#         if i == len(comb_diff)-1:
#             fcomb_diff.write(str(comb_diff[i]))
#         else:
#             fcomb_diff.write(str(comb_diff[i])+'\n')
#     for i in range(len(comb_symdiff)):
#         if i == len(comb_symdiff)-1:
#             fcomb_symdiff.write(str(comb_symdiff[i]))
#         else:
#             fcomb_symdiff.write(str(comb_symdiff[i])+'\n')

        #CHAPTER 3. THE ARRAY ENTERS THE GAME 
print("____________________ARRAY____________________") 
array1 = []
value = random.randint(-10, 10) #число для генерации +-value
for j in range(69420):
    sign = random.randint(-100, 100)
    if sign < 0:
        array1.append((-value))
    else:
        array1.append((value))
    value += random.randint(-50, 50) #шаг чисел
array2 = []
for i in range(80085):
    sign = random.randint(-100, 100)
    if sign < 0:
        array2.append((-value))
    else:
        array2.append((value))
    value += random.randint(-50, 50) #шаг чисел
array1, array2 = sorted(array1), sorted(array2)
# print("\nARRAY1(SHELL)")
# array1, trash_time = shellSort(array1)
# print("\nARRAY2(COMB)")
# array2, trash_time = mycomb(array2)

array = set(array1).union(set(array2))
array_comb = list(array)
array_shell = list(array)
print('\n'+"shell 3.2.2 (USS arr):")
shellSort(array_shell)
print('\n'+"Comb 3.2.2 (USS arr):")
mycomb(array_comb)
print("____________________ARRAY_END____________________\n") 


