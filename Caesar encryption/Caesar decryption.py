LOWER_A_INDEX = ord('a')
LOWER_Z_INDEX  = ord('z')
UPPER_A_INDEX = ord('A')
UPPER_Z_INDEX = ord('Z')


def decrypt(cipher_text, key):
    plain_list = []
    cipher_list = list(cipher_text)
    for character in cipher_list:
        if ord(character) >= LOWER_A_INDEX and ord(character) <= LOWER_Z_INDEX:
            cipher_ord = ord(character)
            plain_ord = cipher_ord - key
            if plain_ord < LOWER_A_INDEX:
                plain_ord += 26
            plain_list.append(chr(plain_ord))
        elif ord(character) >= UPPER_A_INDEX and ord(character) <= UPPER_Z_INDEX:
            cipher_ord = ord(character)
            plain_ord = cipher_ord - key
            if plain_ord < UPPER_A_INDEX:
                plain_ord += 26
            plain_list.append(chr(plain_ord))
        else:
            plain_list.append(character)
    plain_text = ''.join(plain_list)
    return plain_text


def main():
    #ciphertext = raw_input('Please enter the text to be decrypted: ').lower()
    cipher = open("C:\Users\Owner\Documents\jc_encrypted.txt", "r")
    ciphertext = cipher.read()
    key = int(raw_input('Please enter the encryption key used: '))
    print 'The origional text was: {}'.format(decrypt(ciphertext, key))


main()
