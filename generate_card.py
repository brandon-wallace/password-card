#!/usr/bin/env python3

import string
import random
import argparse


parser = argparse.ArgumentParser(description='Create a password card.')
parser.add_argument('--file', type=str, default='password_card.txt',
                    required=False, help='Specify a file name.')
args = parser.parse_args()


def print_header(length):
    '''Print header'''

    return (f'  {" ".join(string.ascii_lowercase[:-7])}\n  {"-"*37}\n')


def print_card():
    '''Print password card'''

    row = 1
    length = 0
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
