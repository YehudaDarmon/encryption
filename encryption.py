def fence_cipher_gen(string):
    for index, char in enumerate(string):
        if index % 2 == 0:
            yield char

    for index, char in enumerate(string):
        if index % 2 != 0:
            yield char        

gen_object = fence_cipher_gen("aharon weber")

print("".join(gen_object))
