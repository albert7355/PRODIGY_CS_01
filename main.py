def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    print("=== Caesar Cipher Tool ===")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().upper()

    message = input("Enter your message: ")
    shift = int(input("Enter shift value (integer): "))

    if choice == 'E':
        encrypted = encrypt(message, shift)
        print(f"Encrypted message: {encrypted}")
    elif choice == 'D':
        decrypted = decrypt(message, shift)
        print(f"Decrypted message: {decrypted}")
    else:
        print("Invalid choice. Please select E or D.")

if _name_ == "_main_":
    main()
