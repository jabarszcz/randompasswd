#!/usr/bin/env python3

import argparse
import string
import random

# Create parser object with program description
parser = argparse.ArgumentParser(
    description="simple script that generates a random password")

# Define program arguments
parser.add_argument("-a", "--lower",	action='store_true',
                    help="add lowercase characters to alphabet")
parser.add_argument("-A", "--upper",	action='store_true',
                    help="add uppercase characters to alphabet")
parser.add_argument("-1", "--num",	action='store_true',
                    help="add digits to alphabet")
parser.add_argument("-s", "--special",	action='store_true',
                    help="add punctuation characters to alphabet")

parser.add_argument("-c", "--characters", action='append', metavar="string",
                    help="add the characters from the given string")

parser.add_argument("-l", "--length", default=10, type=int, metavar ="N",
                    help="length of the password generated")

args = parser.parse_args()

# Create the alphabet
alphabet = ''.join(args.characters) if args.characters else []
if args.lower:
    alphabet += string.ascii_lowercase
if args.upper:
    alphabet += string.ascii_uppercase
if args.num:
    alphabet += string.digits
if args.special:
    alphabet += string.punctuation

if not alphabet:
    print("Alphabet is empty!")
    parser.print_help()
    exit()

passwd = ''.join(random.choice(alphabet) for i in range(args.length))

print(passwd)
