# -*- coding: utf-8 -*-

import itertools
import csv

s = ['s1', 's2']
p = ['p1', 'p2']
h = ['h1', 'h2']
d = ['d1', 'd2']
t = ['t1', 't2']

stores = itertools.product(s, p, h, d, t)

possibilities = []
for store in stores:
    possibilities.extend(list(itertools.permutations(store, len(store))))
# print(possibilities)
# print(len(possibilities))


def get_col(store):
    if store == "s1":
        return 1
    elif store == "s2":
        return 2
    elif store == "p1":
        return 3
    elif store == "p2":
        return 4
    elif store == "h1":
        return 5
    elif store == "h2":
        return 6
    elif store == "d1":
        return 7
    elif store == "d2":
        return 8
    elif store == "t1":
        return 9
    elif store == "t2":
        return 10


def build_distance_array():
    distances = []
    with open('assets/2_2_christmas_shopping.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
            c = []
            for value in row:
                try:
                    c.append(int(value))
                except ValueError:
                    c.append(value.strip())
            distances.append(c)
    return distances


distances = build_distance_array()
travels = []
for possibility in possibilities:
    travel = 0

    # Get work to first store distance
    y = 0

    # Get store to store distances
    for p in possibility:
        x = y
        y = get_col(p)
        travel += distances[x][y]

    # Get last store to home distance
    x = get_col(possibility[-1])
    y = 11
    travel += distances[x][y]

    travels.append({'path': ''.join(possibility),
                    'distance': travel})


travels_sorted = sorted(travels, key=lambda i: i['distance'])
print(travels_sorted[0]['path'])

# Solution : s1d2p2h2t1
