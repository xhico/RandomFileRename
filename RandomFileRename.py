# -*- coding: utf-8 -*-
# !/usr/bin/python3
import os

import random
import string


def random_string():
    rndInt = random.randrange(5, 10)
    str1 = ''.join((random.choice(string.ascii_letters) for x in range(rndInt)))
    str1 += ''.join((random.choice(string.digits) for x in range(rndInt)))

    # It converts the string to list.
    sam_list = list(str1)

    # It uses a random.shuffle() function to shuffle the string.
    random.shuffle(sam_list)

    # Create string
    final_string = ''.join(sam_list)
    return final_string


def main():
    # Get list of all files only in the given directory
    onlyFiles = filter(lambda x: os.path.isfile(os.path.join(FOLDER, x)), os.listdir(FOLDER))

    # Rename files
    for file in onlyFiles:
        src = os.path.join(FOLDER, file)
        dst = os.path.join(FOLDER, random_string())
        print(src)
        print(dst)
        os.rename(src, dst)


if __name__ == "__main__":
    print("----------------------------------------------------")
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    FOLDER = r""

    try:
        main()
    except Exception as ex:
        print(ex)
    finally:
        print("End")
