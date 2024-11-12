from MorseCode import MorseCode

encrypt_messages = True

while encrypt_messages:
    user_input = input("What text would you like converted to Morse Code (q to quit): ").upper()

    if user_input == "Q" or user_input == "QUIT":
        encrypt_messages = False
    else:
        code = MorseCode(user_input)
        print("Your message encrypted to morse code:")
        code.print_message()
        code.decrypt()
        print("Your message decrypted from morse code:")
        code.print_message()
        print("\n")