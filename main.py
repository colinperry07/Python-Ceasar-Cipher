class Caesar():
    
    
    def __init__(self):
        self.LETTERS = 'abcdefghijklmnopqrstuvwxyz'
    
    
    def encrypt(self, message, key):
        encrypted_message = ''
        try:
            for character in self.message:
                character_pos = self.LETTERS.find(character)
                encrypted_message += self.LETTERS[character_pos + self.key]
        except:
            pass
        return encrypted_message


    def decrypt(self, message, key):
        decrypted_message = ''
        try:
            for character in self.message:
                character_pos = self.LETTERS.find(character)
                decrypted_message += self.LETTERS[character_pos - self.key]
        except:
            pass
        return decrypted_message

if __name__ == "__main__":
    cipher = Ceasar()
    
    
    try:
        
        init_message = str(input("Input the message you'd like to encrypt/decrypt: "))
        key_choice = int(input("Enter the key number you would like to encrpyt/decrypt with (1-25): "))
        crypt_choice = str(input("Would you like to encrypt or decrypt the message: "))
        
        if crypt_choice.lower() == "encrypt":
            crypt_choice = True
        if crypt_choice.lower() == "decrypt":
            crypt_choice = False

    except:
        pass
    
    
    if crypt_choice:
        print(cipher.encrypt(init_message.lower(), key_choice))
    else:
        print(cipher.decrypt(init_message.lower(), key_choice))
