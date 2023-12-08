alphabet = [i for i in 'абвгдежзийклмнопрстуфхцчшщъыьэюя']
char_to_num = {char: idx + 1 for idx, char in enumerate(alphabet)}
num_to_char = {idx + 1: char for idx, char in enumerate(alphabet)}
print(char_to_num)

def word_to_number(word):
    word = word.lower()  
    number = 0
    for position, letter in enumerate(reversed(word)):
        digit_value = char_to_num[letter]
        number += digit_value * (32 ** position)
    return number
def number_to_word(number):
    word = ''
    while number > 0:
        number, remainder = divmod(number - 1, 32)
        word = num_to_char[remainder + 1] + word
    return word
original_word = 'бар'
encoded_number = word_to_number(original_word)
print(f"Word '{original_word}' as number: {encoded_number}")

decoded_word = number_to_word(encoded_number)
print(f"Number {encoded_number} as word: '{decoded_word}'")
