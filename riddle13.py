# -*- coding: utf-8 -*-

# A room number must not contain the digits 2-0-2-0 in this order, not even if there are more digits in between.
# For example, these numbers are not allowed any more: 2020, 20201, 205420, 20020, 12101020, whereas these numbers,
# for example, are still ok: 1, 2, 3, 7, 20, 200, 2021, 2002, 10022.
# Oh, and of course, the first room number is 1, not 0.

# What is the room number of the 1,000,000th room ?

import re

pattern = r'[0-9]*2[0-9]*0[0-9]*2[0-9]*0[0-9]*'
h = re.compile(pattern)

rooms = []
i = 0
while len(rooms) <= 1000000:
    if not h.match(str(i)):
        rooms.append(i)
    i += 1

print(rooms[1000000])
# Solution : 1001270
