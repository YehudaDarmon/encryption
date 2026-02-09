from func_encryption import fence_cipher_gen, atbash, random_cipher, caesar_cipher_generator, get_fn

def get_menu_choice():
    """Handles the menu selection and validation"""
    while True:
        print("\n--- Encryption Menu ---")
        print("1. Encrypt using Atbash")
        print("2. Encrypt using Fence Cipher")
        print("3. Encrypt using Random Cipher")
        print("4. Encrypt using Caesar Cipher")
        print("5. Exit")
        
        choice = input("Please select an option (1-5): ")
        if choice in ["1", "2", "3", "4", "5"]:
            return choice
        print("Invalid option, please try again.")

def get_text_input():
    while True:
        text = input("Please enter the text you want to encrypt (letters only): ")
        if text.isalpha():
            return text
        print("Invalid input! Please enter letters only, no numbers or spaces.")

