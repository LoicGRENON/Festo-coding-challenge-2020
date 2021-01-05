# -*- coding: utf-8 -*-

import itertools
import re
from string import ascii_uppercase


def three_words():
    return [''.join(i) for i in itertools.product(ascii_uppercase, repeat=3)]


def get_possible_matches(pattern):
    c = re.compile(pattern)
    return [word for word in three_words() if c.fullmatch(word)]


line1 = get_possible_matches('(R|A|Z)+(AC|AI|CC|CF)+')
print(f"Line 1: {line1}\n---")
line2 = get_possible_matches('(Y|O|C)*K[LI]+')
print(f"Line 2: {line2}\n---")
line3 = get_possible_matches('[^RKC]{0,1}(I|F|ZE|R)+')
print(f"Line 3: {line3}\n---")

col1 = get_possible_matches('[RLY]{1,2}[RCKZ]{1,2}')
col2 = get_possible_matches('[CODNG]+[CHALLENGE]+')
col3 = get_possible_matches('^(?!.*?(.).*?\1)[FESTOAIR]*$')


s1 = set()
for word1 in line1:
    for word2 in col1:
        if word1[0] == word2[0]:
            for word3 in col2:
                if word1[1] == word3[0]:
                    for word4 in col3:
                        if word1[2] == word4[0]:
                            s1.add(word1)

s2 = set()
for word1 in line2:
    for word2 in col1:
        if word1[0] == word2[1]:
            for word3 in col2:
                if word1[1] == word3[1]:
                    for word4 in col3:
                        if word1[2] == word4[1]:
                            s2.add(word1)

s3 = set()
for word1 in line3:
    for word2 in col1:
        if word1[0] == word2[2]:
            for word3 in col2:
                if word1[1] == word3[2]:
                    for word4 in col3:
                        if word1[2] == word4[2]:
                            s3.add(word1)

print(s1)
print(s2)
print(s3)

print([''.join(i) for i in itertools.product(s1, s2, s3)])

# Solution : RCFKLIZER
