# -*- coding: utf-8 -*-

import itertools
import csv

# work > a > b > c > d > e > f > g > h > home
# work > a > b > c > d > e > f > g > h > home
# work >


def letter2num(letter):
    return ord(letter.lower()) - 96


def build_distance_array():
    distances = []
    with open('assets/1_2_christmas_cards.csv', newline='') as csvfile:
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

# friends = "ab"
friends = "abcdefgh"

possibilities = list(itertools.permutations(friends, len(friends)))
distances = build_distance_array()

travels = []
for possibility in possibilities:
    travel = 0

    # Get work to first friend distance
    y = 0

    # Get friend to friend distances
    for p in possibility:
        x = y
        y = letter2num(p)
        travel += distances[x][y]

    # Get last friend to home distance
    x = letter2num(possibility[-1])
    y = 9
    travel += distances[x][y]

    travels.append({'path': ''.join(possibility),
                    'distance': travel})


travels_sorted = sorted(travels, key=lambda i: i['distance'])
print(travels_sorted[0]['path'])

# Solution : hcdfbgea

