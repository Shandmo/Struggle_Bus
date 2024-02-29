# Caesar cipher encrypts letters by shifting them over a certain number of places. The length of shift is called the KEY. If the key is 4, then A becomes E, B becomes F etc.
# ROT 13 is equivalent to a Caesar cipher with a KEY of 13.

try:
    import pyperclip #pyperclip copies text to the clipboard.
except ImportError:
    pass # It's not a big deal if it isn't installed.


SYMBOLS = "ABCDEFGHIJKLMNOPQRTUVWXYZ.!?"

print("Shifts the letters over based off your key number...\n")

while True:
    choice = input("Do you want to (e)ncrypt or (d)ecrypt?\n> ").lower()
    if choice.startswith('e'):
        mode = 'encrypt'
        break
    elif choice.startswith('d'):
        mode = 'decrypt'
        break

while True:
    maxKey = len(SYMBOLS) - 1
    print("Please enter the key (0 to {}) to use.\n> ".format(maxKey))
    response = input('').upper()
    if not response.isdecimal():
        continue

    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break

# Get the message to decrypt or encrypt
print('Enter the message to {}.'.format(mode))
message = input('> ').upper()
# Caesar cipher only works on uppercase letters.

translated = ''

for symbol in message:
    if symbol in SYMBOLS:
        # Get encrypted (or decrypted) number for this symbol
        num = SYMBOLS.find(symbol) # Get the number of the symbol.
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key
        # Handle the wrap-around if num is larger than length of symbols or less than 0:
        if num >= len(SYMBOLS):
            num = num - len(SYMBOLS)
        elif num < 0:
            num = num + len(SYMBOLS)

        # Add encrypted/decrypted number's symbol to translated:
        translated = translated + SYMBOLS[num]
    else:
        # Just add the symbol without encrypting/decrypting:
        translated = translated + symbol
    
# Display the encrypted/decrypted string to the screen:
print(translated)

try:
    pyperclip.copy(translated)
    print('Full {}ed text copied to clipboard'.format(mode))
except:
    pass