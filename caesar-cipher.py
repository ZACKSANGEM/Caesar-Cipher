import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z', ' ']

print(art.logo)

def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        position = alphabet.index(letter)
        new_position = (position + shift_amount) % len(alphabet)
        cipher_text += alphabet[new_position]
    print(f"Here is the encoded text: {cipher_text}")

def decrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        position = alphabet.index(letter)
        new_position = (position - shift_amount) % len(alphabet)
        cipher_text += alphabet[new_position]
    print(f"Here is the decoded text: {cipher_text}")

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)
    else:
        print("Invalid choice.")

    again = input("Type 'yes' if you want to go again. Otherwise type 'no':\n").lower()
    if again == "no":
        should_continue = False
        print("Goodbye, have a great day!")
