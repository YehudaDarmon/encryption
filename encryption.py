import random
import string

def caesar_cipher_generator(string,num_of_shifts):
    abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    
    def ceaser_change(abc_list,shifts,string):
        original_abc_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        adjusted_list = abc_list
        for _ in range(int(shifts)):
            # takes the first letter in list and places it in the end
            adjusted_list.append(adjusted_list.pop(0))
        loop_num = 0
        while loop_num < len(string):
            # gets the position of the letter in a regular abc list and returns the letter from the adjusted abc list
            letter_index = original_abc_list.index(string[loop_num])
            loop_num += 1
            yield adjusted_list[letter_index]

    encrypted_list = ceaser_change(abc,num_of_shifts,string)
    the_encrypted_list = []
    for letter in encrypted_list:
        the_encrypted_list.append(letter)
    return "".join(the_encrypted_list)

def fence_cipher_gen(string):
    
    for index, char in enumerate(string):
        if index % 2 == 0:
            yield char

    for index, char in enumerate(string):
        if index % 2 != 0:
            yield char  

def atbash_generator(user_input):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    cba = 'zyxwvutsrqponmlkjihgfedcba'
    num_1 = '1234567890'
    num_2 = '0987654321'

    for char in user_input:
        if char in abc:
            yield cba[abc.index(char)]
        elif char in num_1:
            yield num_2[num_1.index(char)]
        else:
            yield char  

def random_cipher(str):
    index = 0
    while index<len(str):
        rand = string.ascii_letters + string.digits + string.punctuation
        select = random.choice(rand)
        yield select
        index+=1

def get_fn(user_input,fn):
   reslut = "".join(fn(user_input))
   return reslut


