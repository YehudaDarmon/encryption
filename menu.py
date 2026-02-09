from func_encryption import fence_cipher_gen, atbash, random_cipher
	
def menu_choice():
    print("Welcome to the encryption program")
    on_exit = False
    while not on_exit:
        input_user = input("1. Encrypt using atbash\n2. Encrypt using fence cipher\n3. Encrypt using random cipher\n4. Exit\n")
        if  input_user in ["1","2","3","4"]:
                on_exit = True
                return input_user
        else:
            print("Invalid choice")
            continue

    

def user_input():
	user_input = input("Enter your choice: ")
	return user_input



