from dictionary import DICTIONARY

letter_gap = " "
word_gap = "       "

class MorseCode:

    def __init__(self, message):
        self.message = ""
        self.update_message(message)
        self.encrypt()

    def update_message(self, new_message):
        self.message = new_message.upper()

    def print_message(self):
        print(self.message)

    def encrypt(self):
        encrypted_message = ""
        for letter in self.message:
            if letter == " ":
                encrypted_message += word_gap
            else:
                encrypted_message += DICTIONARY[letter]
                encrypted_message += letter_gap

        self.message = encrypted_message

    def decrypt(self):
        decrypted_message = ""
        citext = ""
        self.message += " "

        for letter in self.message:
            if letter != " ":
                spaces = 0
                citext += letter
            else:
                spaces += 1
                if spaces == 2:
                    decrypted_message += " "
                else:
                    if citext == "": continue
                    decrypted_message += list(DICTIONARY.keys())[list(DICTIONARY.values()).index(citext)]
                    citext = ""
        self.message = decrypted_message