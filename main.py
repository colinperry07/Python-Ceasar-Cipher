class Caesar():
    
    
    def __init__(self):
        self.LETTERS = 'abcdefghijklmnopqrstuvwxyz'
    
    
    def encrypt(self, message, offset):
        encrypted_message = []
        for character in message:
            if character in self.LETTERS:
                character_pos = self.LETTERS.find(character)
                new_pos = (character_pos + offset) % len(self.LETTERS)
                encrypted_message.append(self.LETTERS[new_pos])
            else:
                encrypted_message.append(character)
        return ''.join(encrypted_message)


    def decrypt(self, message, offset):
        decrypted_message = []
        for character in message:
            if character in self.LETTERS:
                character_pos = self.LETTERS.find(character)
                new_pos = (character_pos - offset) % len(self.LETTERS)
                decrypted_message.append(self.LETTERS[new_pos])
            else:
                decrypted_message.append(character)
        return ''.join(decrypted_message)

if __name__ == "__main__":
    cipher = Caesar()
    
    
    try:
        
        init_message = str(input("Input the message you'd like to encrypt/decrypt: "))
        while True:
            offset_choice = int(input("Enter the offset number you would like to encrpyt/decrypt with (1-25): "))
            if 0 > offset_choice > 25:
                offset_choice = None
                print("invalid offset number")
            else:
                break
        crypt_choice = str(input("Would you like to encrypt or decrypt the message: "))
        
        if crypt_choice.lower() == "encrypt":
            crypt_choice = True
        if crypt_choice.lower() == "decrypt":
            crypt_choice = False

    except:
        pass
    
    
    if crypt_choice:
        print(cipher.encrypt(init_message.lower(), offset_choice))
    else:
        print(cipher.decrypt(init_message.lower(), offset_choice))
