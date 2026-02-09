from menu import get_menu_choice, get_text_input
from func_encryption import atbash, fence_cipher_gen, random_cipher, caesar_cipher_generator, get_fn
 


def main():
    choice = get_menu_choice()

    if choice == "5":
        print("Exiting program. Goodbye!")
        exit()

    text_to_encrypt = get_text_input()
    
    result = ""

   
    if choice == "1":
        
        result = get_fn(text_to_encrypt, atbash)
    
    elif choice == "2":
        result = get_fn(text_to_encrypt, fence_cipher_gen)
    
    elif choice == "3":
        result = get_fn(text_to_encrypt, random_cipher)
    
    elif choice == "4":
        while True:
            shift_input = input("Please enter the number of shifts: ")
            if shift_input.isdigit():
                shift_num = int(shift_input)
                break
            print("Please enter a valid integer.")
            
        result = caesar_cipher_generator(text_to_encrypt, shift_num)

    # 5. הדפסת התוצאה הסופית
    print(f"\nOriginal: {text_to_encrypt}")
    print(f"Encrypted: {result}")

if __name__ == "__main__":
    main()

    
