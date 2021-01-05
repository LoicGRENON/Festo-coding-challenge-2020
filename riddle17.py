# -*- coding: utf-8 -*-

from string import ascii_letters, digits
import itertools
import hashlib

available_chars = ascii_letters + digits
brute_force_dict = [''.join(i) for i in itertools.product(available_chars, repeat=2)]
for x in brute_force_dict:
    pwd = 'sQyW' + x + '3w'
    digest = hashlib.md5(pwd.encode('utf8')).hexdigest()
    if digest.startswith('002a8a8b23d03e70'):
        print(pwd)
        break

# Solution : sQyWhn3w
