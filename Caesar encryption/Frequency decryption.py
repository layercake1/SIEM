import os
normal_file = "C:\Users\Owner\Documents\Alice_in_wonderland.txt"
cipher_file = "C:\Users\Owner\Documents\jc_encrypted.txt"
plain_file = "C:\Users\Owner\Documents\Plain_text.txt"
LOWER_A_INDEX = ord('a')
LOWER_Z_INDEX  = ord('z')
UPPER_A_INDEX = ord('A')
UPPER_Z_INDEX = ord('Z')


def get_frequency(text):
    frequency_list = []
    for i in range(0, 26):
        frequency_list.append(0.0)
    text = text.lower()
    text_length = 0
    for letter in text:
        if ord(letter) < 97 or ord(letter) > 122:
            continue
        frequency_list[ord(letter) - 97] += 1
        text_length += 1
    for i in range(0, len(frequency_list)):
        frequency_list[i] /= text_length
    return frequency_list


def sum_of_squared_differences(list1, list2):
    ssd = 0
    for i in range(0, len(list1)):
        diff = list1[i] - list2[i]
        ssd += diff * diff
    return ssd


def try_all_shifts(cipher, plain):
    ssd_list = []
    for i in range(0, 25):
        ssd_list.append(sum_of_squared_differences(cipher, plain))
        cipher.append(cipher.pop(0))
    return ssd_list


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
    normal_text = open(normal_file, "r")
    plain_text = open(plain_file, "w")
    cipher_frequency = get_frequency(cipher_text.read())
    normal_frequency = get_frequency(normal_text.read())
    all_shifts = try_all_shifts(cipher_frequency, normal_frequency)
    lowest_ssd = [1, 0]
    for item in range(0, len(all_shifts)):
        if all_shifts[item] < lowest_ssd[0]:
            lowest_ssd = [all_shifts[item], item]
    cipher_text.seek(0)
    plain_text.truncate()
    plain_text.write(decrypt(cipher_text.read(), lowest_ssd[1]))
    plain_text.close()
    os.system("start " + str(plain_file))
    print 'Key is {}'.format(lowest_ssd[1])


main()
