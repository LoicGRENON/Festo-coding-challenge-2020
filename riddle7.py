# -*- coding: utf-8 -*-

# Room numbers must contain a digit 5 or a digit 7, but not both of them
# 5, 17, 52, 55, 177 are all valid room numbers, but 24, 157 or 7005 are not.
# What is the room number of the 1000th room?

# import itertools
# import string
#
# valid_digits = string.digits
#
# # x = list(map(''.join, itertools.permutations(string.ascii_lowercase, 5)))
# x = list(map(''.join, itertools.combinations(valid_digits, 2)))
#
# print(x)

rooms = []
number = 0
while len(rooms) < 1000:
    if '5' in str(number) and '7' not in str(number):
        rooms.append(number)
    if '7' in str(number) and '5' not in str(number):
        rooms.append(number)
    number += 1

print(rooms[999])
# Solution : 2379
