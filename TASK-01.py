# Function to perform Caesar Cipher encryption
def encrypt_caesar(text, shift):
    result = ""
    
    for char in text:
        if char.isupper():  # Encrypt uppercase letters
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():  # Encrypt lowercase letters
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:  # Keep non-alphabetical characters unchanged
            result += char

    return result

# Function to perform Caesar Cipher decryption
def decrypt_caesar(text, shift):
    result = ""
    
    for char in text:
        if char.isupper():  # Decrypt uppercase letters
            result += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():  # Decrypt lowercase letters
            result += chr((ord(char) - shift - 97) % 26 + 97)
        else:  # Keep non-alphabetical characters unchanged
            result += char

    return result

# Function to get a valid shift value from the user
def get_shift_value():
    while True:
        try:
            shift = int(input("Enter the shift value (positive integer): "))
            if shift < 0:
                print("Please enter a positive integer.")
            else:
                return shift
        except ValueError:
            print("Invalid input. Please enter an integer.")

# Main function to interact with the user
def main():
    print("Welcome to the Caesar Cipher program!")
    
    while True:
        action = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().upper()
        if action not in ['E', 'D']:
            print("Invalid choice. Please choose 'E' for encryption or 'D' for decryption.")
            continue
        
        message = input("Enter the message: ").strip()
        shift = get_shift_value()
        
        if action == 'E':
            encrypted_message = encrypt_caesar(message, shift)
            print(f"Encrypted message: {encrypted_message}")
        elif action == 'D':
            decrypted_message = decrypt_caesar(message, shift)
            print(f"Decrypted message: {decrypted_message}")
        
        repeat = input("Do you want to perform another operation? (Y/N): ").strip().upper()
        if repeat != 'Y':
            print("Goodbye!")
            break

# Run the main function to start the program
if _name_ == "_main_":
    main()
