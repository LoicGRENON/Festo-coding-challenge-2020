# -*- coding: utf-8 -*-

import itertools
import hashlib
from string import ascii_letters, digits


available_chars = ascii_letters + digits
brute_force_dict = [''.join(i) for i in itertools.product(available_chars, repeat=2)]

possibilities = []
brute_force_words = itertools.product(['n0'], ['qg'], brute_force_dict, brute_force_dict)
for trial, product_list in enumerate(brute_force_words, 1):
    for permutation_list in itertools.permutations(product_list, 4):
        pwd = ''.join(permutation_list)
        print(f"Try #{trial}: {pwd} ...")
        digest = hashlib.md5(pwd.encode('utf8')).hexdigest()
        if digest.startswith('a84ba651fd122ef5'):
            print(f"Password found ! {pwd}")
            exit()
        trial += 1
