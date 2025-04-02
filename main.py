class Caesar():
    
    
    def __init__(self):
        self.LETTERS = 'abcdefghijklmnopqrstuvwxyz'
    
    
    def encrypt(self, message, key):
        encrypted_message = []=
        for character in message:
            if character in self.LETTERS:
                character_pos = self.LETTERS.find(character)
                new_pos = (character_pos + key) % len(self.LETTERS)
                encrypted_message.append(self.LETTERS[new_pos])
            else:
                encrypted_message.append(character)
        return ''.join(encrypted_message)


    def decrypt(self, message, key):
        decrypted_message = []=
        for character in message:
            if character in self.LETTERS:
                character_pos = self.LETTERS.find(character)
                new_pos = (character_pos + key) % len(self.LETTERS)
                decrypted_message.append(self.LETTERS[new_pos])
            else:
                decrypted_message.append(character)
        return ''.join(decrypted_message)

if __name__ == "__main__":
    cipher = Ceasar()
    
    
    try:
        
        init_message = str(input("Input the message you'd like to encrypt/decrypt: "))
        while True:
            key_choice = int(input("Enter the key number you would like to encrpyt/decrypt with (1-25): "))
            if 0 > key_choice > 25:
                key_choice = None
                print("invalid key number")
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
        print(cipher.encrypt(init_message.lower(), key_choice))
    else:
        print(cipher.decrypt(init_message.lower(), key_choice))
