# -*- coding: utf-8 -*-
# !/usr/bin/python3

import os
import random
import string


def generate_random_string(length):
    # generates a random string of specified length
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


def rename_files(folder_path):
    # get a list of all files only in the given directory
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    # rename files
    for file in files:
        src = os.path.join(folder_path, file)
        dst = os.path.join(folder_path, generate_random_string(random.randint(5, 10)))
        print(f'Renaming {src} to {dst}')
        os.rename(src, dst)


if __name__ == "__main__":
    print("----------------------------------------------------")
    # change the current working directory to the directory of the script
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    try:
        folder_path = input("Enter folder path: ")
        rename_files(folder_path)
    except Exception as ex:
        print(ex)
    finally:
        print("End")
