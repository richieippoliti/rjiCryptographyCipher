import string

def encrypt(message, key):

    shift = key % 26
    cipher = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift])

    encrypted_message = message.lower().translate(cipher)

    return encrypted_message

def decrypt(encrypted_message, key):

    shift = 26 - (key % 26)
    cipher = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift])

    message = encrypted_message.translate(cipher)
    return message

def main():
    while True:
        print("Caesar Cipher Encryptor / Decryptor. Please Select an Option Below:")
        print("---")
        print("1. Encrypt a Message")
        print("2. Decrypt a Message")
        print("3. Exit")
        print("---")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            message = input("Enter the message you wish to encrypt: ")
            try:
                key = int(input("Enter the key (integer): "))
                encrypted_message = encrypt(message, key)
                print('-')
                print(f"Encrypted Message: {encrypted_message}")
                print('-')
            except ValueError:
                print("Invalid key. Please enter an integer.")

        elif choice == '2':
            encrypted_message = input("Enter the message you wish to decrypt: ")
            try:
                key = int(input("Enter the key (integer): "))
                decrypted_message = decrypt(encrypted_message, key)
                print('-')
                print(f"Decrypted Message: {decrypted_message}")
                print('-')
            except ValueError:
                print("Invalid key. Please enter an integer.")

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select option 1, 2, or 3.")

if __name__ == "__main__":
    main()
