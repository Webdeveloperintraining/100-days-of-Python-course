import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)

def caesar(text,shift,direction):
    alphabet_number = len(alphabet) - 1
    end_text=''
    for i in text:
        if i not in alphabet:
            end_text += i
            continue
        if direction.lower() == 'encode':
            letter_index = (alphabet.index(i) + (shift % 26) ) % 26
        elif direction.lower() == 'decode':
            letter_index = (alphabet.index(i) - (shift % 26) ) % 26
        elif letter_index > alphabet_number:
           letter_index -= alphabet_number + 1
        end_text += alphabet[letter_index]
    print(f"The {direction}d text is: {end_text}")

repeat = 'y'
while repeat == 'y':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text,shift,direction)
    repeat = input('Restart the cipher program? (y/n) ')
















# def encrypt(text,shift):
#     alphabet_number = len(alphabet) - 1
#     cipher_text=''
#     for i in text:
#         letter_index = alphabet.index(i) + shift
#         if letter_index > alphabet_number:
#            letter_index -= alphabet_number+1
#         cipher_text += alphabet[letter_index]
#     print(f"The encoded text is: {cipher_text}")

# def decrypt(text,shift):
#     alphabet_number = len(alphabet) - 1
#     plain_text=''
#     for i in text:
#         letter_index = alphabet.index(i) - shift
#         if letter_index > alphabet_number:
#            letter_index -= alphabet_number+1
#         plain_text += alphabet[letter_index]
#     print(f"The decoded text is: {plain_text}")

# if direction.lower() == 'encode':
#     encrypt(text,shift)
# elif direction.lower() == 'decode':
#     decrypt(text,shift)


