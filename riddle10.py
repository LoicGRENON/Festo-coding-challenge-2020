# -*- coding: utf-8 -*-

import hashlib

for i in range(100, 1000):
    pwd = i * 1000000000 + 726300631
    digest = hashlib.md5(str(pwd).encode('utf8')).hexdigest()
    if digest.startswith('351635d71448baca'):
        print(pwd)
        break

# Solution : 431726300631
