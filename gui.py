"""Encryption GUI - A3."""
from guizero import App, Text, TextBox, Slider, PushButton, ButtonGroup

alphabet = "abcdefghijklmnopqrstuvwxyz"


def action():
    """
    Triggered when user pushes 'Do it!' button.

    Checks if message should be encrypted or decrypted.
    """
    inp = choice.value
    m = message.value.lower()
    k = sld_key.value
    out = ""

    # check what was selected: "encrypt" or "decrypt"
    if inp == "E":
        out = encrypt(m, k)
    elif inp == "D":
        out = decrypt(m, k)

    message.value = str(out)


def encrypt(message, key):
    """Encrypt the message given."""
    eMessage = ''
    for char in message:
        if char in alphabet:
            position = alphabet.find(char)
            newPosition = (position + (key * 1)) % 26
            newChar = alphabet[newPosition]
            eMessage += newChar
        else:
            eMessage += char

    return eMessage


def decrypt(message, key):
    """Decrypt the message given."""
    dMessage = ''
    for char in message:
        if char in alphabet:
            position = alphabet.find(char)
            newPosition = (position + (key * (-1))) % 26
            newChar = alphabet[newPosition]
            dMessage += newChar
        else:
            dMessage += char

    return dMessage


app = App(title="GUI Encryptor", width=250, height=180, layout="grid")

# label and input for user's message
txt_input = Text(app, text="Enter your message:", grid=[0, 0], align="top")
message = TextBox(app, grid=[0, 1], width=41)

# label and slider for an encryption key
txt_key = Text(app, text="Pick a key:", grid=[0, 2], align="top")
sld_key = Slider(app, grid=[0, 3], start=1, end=26, align="top")

# button group to select Encryption or Decryption
choice = ButtonGroup(app, options=[["Encrypt", "E"], ["Decrypt", "D"]],
                     selected="E", horizontal=True, grid=[0, 4], align="top")

# button for making things happen
btn = PushButton(app, command=action, text="Do it!", grid=[0, 5],
                 align="top")

app.display()
