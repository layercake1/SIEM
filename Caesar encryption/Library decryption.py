import os
common_words_file = "C:\Users\Owner\Documents\common_words.txt"
cipher_file = "C:\Users\Owner\Documents\jc_encrypted.txt"
plain_file = "C:\Users\Owner\Documents\Plain_text.txt"
LOWER_A_INDEX = ord('a')
LOWER_Z_INDEX  = ord('z')
UPPER_A_INDEX = ord('A')
UPPER_Z_INDEX = ord('Z')


def count_common_words(cipher, cw):
    common_words_list = cw.split()
    cw_count = 0
    for item in common_words_list:
        cw_count += cipher.lower().count(item)
    return cw_count


def try_all_shifts(cipher, cw):
    cw_count_list = []
    for i in range(0, 25):
        cipher_shifted = decrypt(cipher, i)
        cw_count_list.append(count_common_words(cipher_shifted.lower(), cw))
    return cw_count_list


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
    cipher_text = open(cipher_file, "r")
    common_words_text = open(common_words_file, "r")
    plain_text = open(plain_file, "r+")
    all_shifts = try_all_shifts(cipher_text.read(), common_words_text.read())
    highest_cw_count = [0, 0]
    for item in range(0, len(all_shifts)):
        if all_shifts[item] > highest_cw_count[0]:
            highest_cw_count = [all_shifts[item], item]
    cipher_text.seek(0)
    plain_text.truncate()
    plain_text.write(decrypt(cipher_text.read(), highest_cw_count[1]))
    plain_text.close()
    cipher_text.seek(0)
    os.system("start " + str(plain_file))
    print 'Key is {}'.format(highest_cw_count[1])


main()
