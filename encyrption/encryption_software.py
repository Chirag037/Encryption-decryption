#!/usr/bin/env python3
"""
Simple Encryption/Decryption Software
Caesar cipher implementation for text and file encryption
"""

def encrypt_text(text, shift):
    """Encrypt text using Caesar cipher"""
    encrypted = ""
    
    for char in text:
        if char.isalpha():
            if char.isupper():
                encrypted += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            encrypted += char
    
    return encrypted

def decrypt_text(text, shift):
    """Decrypt text using Caesar cipher"""
    return encrypt_text(text, -shift)

def encrypt_file(input_file, output_file, shift):
    """Encrypt file contents"""
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        encrypted_content = encrypt_text(content, shift)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(encrypted_content)
        
        print(f"File encrypted successfully: {output_file}")
    
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"Error encrypting file: {e}")

def decrypt_file(input_file, output_file, shift):
    """
    Decrypt contents of a file
    
    Args:
        input_file (str): Path to encrypted file
        output_file (str): Path to output file
        shift (int): Decryption shift value
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        decrypted_content = decrypt_text(content, shift)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(decrypted_content)
        
        print(f"File decrypted successfully: {output_file}")
    
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"Error decrypting file: {e}")

def brute_force_decrypt(text):
    """
    Try all possible shift values to decrypt text
    
    Args:
        text (str): Encrypted text to decrypt
    """
    print("Trying all possible shift values:")
    print("-" * 40)
    
    for shift in range(26):
        decrypted = decrypt_text(text, shift)
        print(f"Shift {shift:2d}: {decrypted}")

def main():
    """
    Main function to run the encryption/decryption software
    """
    print("=== Simple Encryption/Decryption Software ===")
    print("Using Caesar Cipher")
    print()
    
    while True:
        print("Options:")
        print("1. Encrypt text")
        print("2. Decrypt text")
        print("3. Encrypt file")
        print("4. Decrypt file")
        print("5. Brute force decrypt")
        print("6. Exit")
        
        choice = input("\nChoose an option (1-6): ").strip()
        
        if choice == '1':
            text = input("Enter text to encrypt: ")
            try:
                shift = int(input("Enter shift value (1-25): "))
                if 1 <= shift <= 25:
                    encrypted = encrypt_text(text, shift)
                    print(f"Encrypted text: {encrypted}")
                else:
                    print("Shift value must be between 1 and 25.")
            except ValueError:
                print("Invalid shift value. Please enter a number.")
        
        elif choice == '2':
            text = input("Enter text to decrypt: ")
            try:
                shift = int(input("Enter shift value (1-25): "))
                if 1 <= shift <= 25:
                    decrypted = decrypt_text(text, shift)
                    print(f"Decrypted text: {decrypted}")
                else:
                    print("Shift value must be between 1 and 25.")
            except ValueError:
                print("Invalid shift value. Please enter a number.")
        
        elif choice == '3':
            input_file = input("Enter input file path: ")
            output_file = input("Enter output file path: ")
            try:
                shift = int(input("Enter shift value (1-25): "))
                if 1 <= shift <= 25:
                    encrypt_file(input_file, output_file, shift)
                else:
                    print("Shift value must be between 1 and 25.")
            except ValueError:
                print("Invalid shift value. Please enter a number.")
        
        elif choice == '4':
            input_file = input("Enter encrypted file path: ")
            output_file = input("Enter output file path: ")
            try:
                shift = int(input("Enter shift value (1-25): "))
                if 1 <= shift <= 25:
                    decrypt_file(input_file, output_file, shift)
                else:
                    print("Shift value must be between 1 and 25.")
            except ValueError:
                print("Invalid shift value. Please enter a number.")
        
        elif choice == '5':
            text = input("Enter encrypted text to brute force: ")
            brute_force_decrypt(text)
        
        elif choice == '6':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select 1-6.")
        
        print()

if __name__ == "__main__":
    main()
