import random,time,string
###############################################################################################
'''
i open file. i read it. i get a massive string. i make an array of words from it. i make two lists. one is unique values(set) second is just values.
i sort them values. i set to numbers using dict. then with that dict i go and convert my list to numbers such as key -> val. 
then search compares value inside the list to the key if they match then i count that word, create a new dict where theres word and its count.
'''

word_num = {}
alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
alphabet = [i for i in alphabet]
    
def hunting_search_Kirde(list,key): #search itself
    high = len(list)-1 # задача границ, как и в почти каждом другом поиске
    freq = 0
    i = 0
    # count = 0 # будущий счетчик на сравнения в цикле, пока он возвращает ноль
    while key in list:
        try:
            while key <= list[high]: # index error maybe
                # print('идём влево')
                if key == list[high]:
                    freq += 1
                    list.pop(high)
                    i = 0
                    break
                high -= 2**i
                i += 1
        except IndexError:
            high = 0 # now high is low
        try:
            while key >= list[high]:
                # print('идём ВПРАВО')
                if key == list[high]:
                    freq += 1
                    list.pop(high)
                    i = 0
                    break
                high += 2**i
                i += 1
        except IndexError:
            high = len(list)-1
    return freq

#MAIN   
with open('FINarticle.txt',encoding="utf-8" ) as space:
    Billy = space.read().lower()
    Billy = Billy.replace('ё','е')
    Billy_clean = ''
    for i in Billy:
        if i not in alphabet:
            Billy_clean += ' '
        else:
            Billy_clean += i
    Billy_clean = Billy_clean.split()
    Billy_clean = [string for string in Billy_clean if len(string) >= 4]

    Billy_clean = sorted(Billy_clean)
    bilset = sorted(list(set(Billy_clean)))
    
    print(bilset,'\n')
    for i in bilset:
        word_num[i] = len(word_num)
    print(word_num, '\n')
    word_freq = word_num
    keys = []
    for i in Billy_clean:
        keys.append(word_num[i])
    for j in bilset:
        val = word_num[j]
        word_freq[j] = hunting_search_Kirde(keys, val)
    sorted_freq = dict(sorted(word_freq.items(), key=lambda item: item[1])) 
    print(sorted_freq)