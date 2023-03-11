# -*- coding: utf-8 -*-
# !/usr/bin/python3

import os
import random
import string


def generate_random_string(length):
    """
    Returns a random string of specified length.

    Args:
        length (int): The length of the string to generate.

    Returns:
        str: A random string of the specified length.

    """
    # Define a set of characters to use in the string
    characters = string.ascii_letters + string.digits

    # Generate a random string of the specified length using the characters
    random_string = ''.join(random.choice(characters) for _ in range(length))

    # Return the random string
    return random_string


def rename_files():
    """
    Rename all files in a given folder_path by generating a random string for each file name.

    Args:
        folder_path (str): The path to the directory containing the files to be renamed.

    Returns:
        None: This function does not return anything, but it will print out the old and new file names for each file.

    Raises:
        FileNotFoundError: If the folder_path does not exist or cannot be found.

    """
    # get a list of all files only in the given directory
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    # rename files
    for file in files:
        src = os.path.join(folder_path, file)
        # generate a random string for the new file name
        dst = os.path.join(folder_path, generate_random_string(random.randint(5, 10)))
        # print the old and new file names for each file
        print(f'Renaming {src} to {dst}')
        # rename the file
        os.rename(src, dst)


if __name__ == "__main__":
    print("----------------------------------------------------")
    # change the current working directory to the directory of the script
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    try:
        folder_path = input("Enter folder path: ")
        rename_files()
    except Exception as ex:
        print(ex)
    finally:
        print("End")
