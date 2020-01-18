"""Secret Messages."""
alphabet = "abcdefghijklmnopqrstuvwxyz"
message = input("Please enter your message:").lower()


def encrypt(message, key):
    eMessage = ''
    for character in message:
        if character in alphabet:
            position = alphabet.find(character)
            newPosition = (position + (key * 1)) % 26
            newCharacter = alphabet[newPosition]
            eMessage += newCharacter
        else:
            eMessage += character

    print(eMessage)


def decrypt(message, key):
    dMessage = ''
    for character in message:
        if character in alphabet:
            position = alphabet.find(character)
            newPosition = (position + (key * (-1))) % 26
            newCharacter = alphabet[newPosition]
            dMessage += newCharacter
        else:
            dMessage += character

    print(dMessage)


while True:
    key = input("Please enter a key from 1 to 26:")

    if key.isdigit() is False:
        print("Your key should be a number!")
        continue
    elif int(key) < 1 or int(key) > 26:
        print("Key should be in teh range from 1 to 26!")
        continue
    else:
        key = int(key)

        while True:
            answer = input("(E)ncrypt or (D)ecrypt?").lower()

            if answer != 'e' and answer != 'd':
                print("Invalid Input! Please enter 'E','e','d' or 'D' ")
                continue
            else:
                if answer == 'e':
                    encrypt(message, key)
                    break
                elif answer == 'd':
                    decrypt(message, key)
                    break
        break
