import art

def decrypt_message(text,shift):
    decrypted_message=''
    for char in text:
        for char_index in range(0,len(alphabet)):
            if char is alphabet[char_index]:
                decrypted_message+=alphabet[(char_index-shift)%26]
    print(f"decrypted message is {decrypted_message}")
        
def encrypt_message(text,shift):
    encrypted_message=''
    
    for char in text:
        for char_index in range(0,len(alphabet)):
            if char is alphabet[char_index]:
                encrypted_message+=alphabet[(char_index+shift)%26]
    print(f"encrypted message is {encrypted_message}")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(art.logo)
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction =='decode':
        decrypt_message(text,shift)
    else:
        encrypt_message(text,shift)

    choice=input("type yes if you want to go again,else type no: ")
    if choice.lower() =='yes':
        continue
    else:
        break
