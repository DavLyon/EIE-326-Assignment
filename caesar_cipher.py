def caesar_cipher(text, shift, mode='encrypt'):
    """
    Implement a Caesar cipher encryption and decryption.
    
    Args:
        text (str): The text to encrypt or decrypt
        shift (int): The shift value (key) for the cipher
        mode (str): 'encrypt' or 'decrypt'
    
    Returns:
        str: The encrypted or decrypted text
    """
    # Normalize shift value to be between 0-25
    shift = shift % 26
    
    # If decrypting, reverse the shift
    if mode.lower() == 'decrypt':
        shift = -shift
    
    result = ""
    
    for char in text:
        # Check if the character is a letter
        if char.isalpha():
            # Determine ASCII offset (65 for uppercase, 97 for lowercase)
            ascii_offset = 65 if char.isupper() else 97
            
            # Convert to 0-25 range, apply shift, and wrap around with modulo
            shifted_position = (ord(char) - ascii_offset + shift) % 26
            
            # Convert back to ASCII and then to character
            result += chr(shifted_position + ascii_offset)
        else:
            # Keep non-alphabetic characters unchanged
            result += char
    
    return result

def main():
    print("Caesar Cipher Implementation")
    print("===========================")
    
    while True:
        print("\nChoose an option:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Brute force decrypt (try all shifts)")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '1':
            text = input("Enter the message to encrypt: ")
            while True:
                try:
                    shift = int(input("Enter the shift value (1-25): "))
                    if 1 <= shift <= 25:
                        break
                    print("Shift must be between 1 and 25.")
                except ValueError:
                    print("Please enter a valid number.")
            
            encrypted = caesar_cipher(text, shift, 'encrypt')
            print(f"\nEncrypted message: {encrypted}")
            
        elif choice == '2':
            text = input("Enter the message to decrypt: ")
            while True:
                try:
                    shift = int(input("Enter the shift value (1-25): "))
                    if 1 <= shift <= 25:
                        break
                    print("Shift must be between 1 and 25.")
                except ValueError:
                    print("Please enter a valid number.")
            
            decrypted = caesar_cipher(text, shift, 'decrypt')
            print(f"\nDecrypted message: {decrypted}")
            
        elif choice == '3':
            text = input("Enter the encrypted message: ")
            print("\nTrying all possible shifts:")
            
            for shift in range(1, 26):
                decrypted = caesar_cipher(text, shift, 'decrypt')
                print(f"Shift {shift}: {decrypted}")
            
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
