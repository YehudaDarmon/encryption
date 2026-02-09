def atbash(user_input):
    abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    cba = ['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a']
    num_1 = ['1','2','3','4','5','6','7','8','9','0']
    num_2 = ['0','9','8','7','6','5','4','3','2','1']
    atbash_pass = []
    for letter in user_input:
        if letter in abc:
            index = abc.index(letter)
            atbash_pass.append(cba[index])
        elif letter in num_1:
            index = num_1.index(letter)
            atbash_pass.append(num_2[index])
    return "".join(atbash_pass)
