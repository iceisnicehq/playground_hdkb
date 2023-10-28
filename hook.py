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


