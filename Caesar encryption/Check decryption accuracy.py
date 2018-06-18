import os
original_file = "C:\Users\Owner\Documents\Julius_Caesar.txt"
decrypted_file = "C:\Users\Owner\Documents\Plain_text.txt"


def check(file1, file2):
    if os.path.getsize(file1) == os.path.getsize(file2):
        if open(file1,'r').read() == open(file2,'r').read():
            return "All is correct"
    return "There are inacurracies in this decryption"


def main():
    print check(original_file, decrypted_file)


main()
