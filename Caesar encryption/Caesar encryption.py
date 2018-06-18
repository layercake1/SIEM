import random
LOWER_A_INDEX = ord('a')
LOWER_Z_INDEX  = ord('z')
UPPER_A_INDEX = ord('A')
UPPER_Z_INDEX = ord('Z')

def encrypt(plain_text, key):
    cipher_list = []
    plain_list = list(plain_text)
    for index in plain_list:
        if ord(index) >= LOWER_A_INDEX and ord(index) <= LOWER_Z_INDEX:
            plain_ord = ord(index)
            cipher_ord = plain_ord + key
            if cipher_ord > LOWER_Z_INDEX:
                cipher_ord -= 26
            cipher_list.append(chr(cipher_ord))
        elif ord(index) >= UPPER_A_INDEX and ord(index) <= UPPER_Z_INDEX:
            plain_ord = ord(index)
            cipher_ord = plain_ord + key
            if cipher_ord > UPPER_Z_INDEX:
                cipher_ord -= 26
            cipher_list.append(chr(cipher_ord))
        else:
            cipher_list.append(index)
    cipher_text = ''.join(cipher_list)
    return cipher_text


def main():
    plain_file = open("C:\Users\Owner\Documents\Julius_Caesar.txt", "r")
    plaintext = plain_file.read()
    key = random.randint(1, 25)
    cipher_file = open("C:\Users\Owner\Documents\jc_encrypted.txt", "w")
    cipher_file.write(encrypt(plaintext, key))
    cipher_file.close()
    print 'Encrypted using {} as key'.format(key)


main()