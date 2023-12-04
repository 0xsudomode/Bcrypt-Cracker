#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from passlib.hash import bcrypt
import sys

color = "\033[38;5;10m"   # Green color
colorr = "\033[38;5;202m"  # Orange color

def crack_password(hash, word_list, hash_index):
    length = len(word_list)
    correct_word = ""
    found = 0

    for (index, word) in enumerate(word_list, start=1):
        print(f"\r{color}Wait: {hash_index}/{length} Hashes complete | Wordlist Line: {index}/{length} Words complete", end='', flush=True)
        correct = bcrypt.verify(word, hash)
        if correct:
            correct_word = word
            found += 1
            break

    print()  

    if found == 1:
        print(f"{colorr}\n\nPassword found for Hash:", hash)
        print(f"{color}Results:", correct_word)
    else:
        print(f"{color}\n\nPassword not found for Hash {hash}.")

def main():
    parser = argparse.ArgumentParser(description="Bcrypt-Cracker - Bcrypt simple hash cracker in python !")
    parser.add_argument("-s", "--single", help="Specify a single hash to crack", metavar="HASH")
    parser.add_argument("-i", "--input", help="Input file containing hash or hashes", metavar="FILE")
    parser.add_argument("-w", "--wordlist", help="Wordlist file for password cracking", metavar="FILE", required=True)
    args = parser.parse_args()

    if args.single:
        try:
            with open(args.wordlist, "r", encoding="cp437") as wordlist_file:
                words = wordlist_file.read().splitlines()
        except FileNotFoundError:
            print(f"{color}Error: File {args.wordlist} not found.")
            sys.exit(1)

        crack_password(args.single, words, 1)
    elif args.input:
        try:
            with open(args.input, "r", encoding="cp437") as input_file:
                hashes = input_file.read().splitlines()
        except FileNotFoundError:
            print(f"{color}Error: File {args.input} not found.")
            sys.exit(1)

        try:
            with open(args.wordlist, "r", encoding="cp437") as wordlist_file:
                words = wordlist_file.read().splitlines()
        except FileNotFoundError:
            print(f"{color}Error: File {args.wordlist} not found.")
            sys.exit(1)

        for hash_index, hash_to_crack in enumerate(hashes, start=1):
            crack_password(hash_to_crack, words, hash_index)
    else:
        print(f"{color}Error: Either -i or -s is required.")
        sys.exit(1)

if __name__ == "__main__":
    print(f"{color}\n*************************************************")
    print(f"{color}Bcrypt-Cracker - Bcrypt hash cracker | [sudomode]")
    print(f"{color}*************************************************")
    main()
