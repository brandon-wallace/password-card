#!/usr/bin/env python3
'''

Create a password card.

Requirements:
    Python3.6+

'''

import string
import random
import argparse
from pathlib import Path


parser = argparse.ArgumentParser(description='Create a password card.')
parser.add_argument('--file', type=str, default='password_card.txt',
                    required=False, help='Specify a file name.')
args = parser.parse_args()


def overwrite_existing_file(file):
    '''Check if file is existing'''

    if Path(file).is_file():
        overwrite = input('Overwrite existing password-card.txt file? (Yes or No) ')
        if overwrite.lower().startswith('y'):
            print(f'Overwriting {file} file!')
        else:
            args.file = input('Enter a filename: ')
            print(f'Creating new file {args.file}!')
    else:
        return


def print_header(length):
    '''Print header'''

    return (f'  {" ".join(string.ascii_lowercase[:-7])}\n  {"-"*37}\n')


def print_card():
    '''Print password card'''

    row = 1
    length = 0
    overwrite_existing_file(args.file)
    with open(args.file, 'w') as file:
        file.write(str(print_header(19)))
        chars = string.printable[:-6]
        chars = list(chars)
        random.shuffle(chars)
        file.write(f'{row}')
        for a in chars:
            length += 1
            file.write(f' {a}')
            if length % 19 == 0:
                file.write('\n\n')
                row += 1
                file.write(f'{row}')


print_card()
