import random
import string

def random_cipher(str):
    index = 0
    while index<len(str):
        rand = string.ascii_letters + string.digits + string.punctuation
        select = random.choice(rand)
        yield select
        index+=1
#השורות הבאות הן בדיקה לפני המירגוג יש למחוק שורות אלו
encryption_random = random_cipher("yakov")
for litle in encryption_random:
    print(litle)