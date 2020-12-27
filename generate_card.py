#!/usr/bin/env python3

import string
import random


def print_header(length):
    print(' ', end='')
    for a in range(length):
        print(f' {"".join(string.ascii_lowercase)[a]}', end='')
    print('\n')


def print_card():
    row = 1
    length = 0
    print_header(19)
    chars = string.printable[:-6]
    chars = list(chars)
    random.shuffle(chars)
    print(f'{row}', end='')
    for a in chars:
        length += 1

        print(f' {a}', end='')
        if length % 19 == 0:
            print('\n')
            row += 1
            print(f'{row}', end='')


print_card()
