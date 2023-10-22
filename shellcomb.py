
def shellSort(array):
    n = len(array)
    k = n//2
    interval = 2**k -1
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp
        k -= 1
        interval = 2**k -1
    return array
def mycomb(arr):
    gap = int(len(arr))
    swap = True

    while gap > 1 or swap:
        gap = int(gap/1.3)
        swap = False
        for i in range(len(arr)-gap):
            if arr[i]>arr[i+gap]:
                arr[i], arr[i+gap] = arr[i+gap], arr[i]
                swap = True
    return arr

with open("text1.txt", "r") as file_in, open("shell.txt", "w") as file_out:
    # Read numbers from file
    numbers = [line.strip() for line in file_in]
    try:
        numbers = [int(i) for i in numbers]
    except ValueError:
        pass
        # Sort numbers
    shellSort(numbers)

    # Write sorted numbers to a file
    maximum = max(numbers)
    print(maximum)
    for number in numbers:
        file_out.write(str(number))
        if number != maximum:
            file_out.write('\n')
with open("text2.txt", "r") as file_in, open("comb.txt", "w") as file_out:
    # Read numbers from file
    numbers = [line.strip() for line in file_in]
    try:
        numbers = [int(i) for i in numbers]
    except ValueError:
        pass
        # Sort numbers
    shellSort(numbers)

    # Write sorted numbers to a file
    maximum = str(max(numbers))
    print(maximum)
    for number in numbers:
        file_out.write(str(number))
        if number != maximum:
            file_out.write('\n')
        


