import random
import string
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

def get_fn(user_input,fn):
   reslut = "".join(fn(user_input))
   return reslut

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


