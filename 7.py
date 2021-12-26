#!/usr/local/bin/python3

import numpy
from numpy import median

test_raw = """16,1,2,0,4,2,7,1,2,14"""

test = list(list(map(int, test_raw.split(","))))
real = list(list(map(int, open("7.txt").read().split(","))))

def move_crabs(crabs, target, constant_drain = True):

    fuel_cost = 0

    for crab in crabs:
        if constant_drain:
            fuel_cost += abs(crab - target)
        else:
            n = abs(crab - target)
            fuel_cost += (n * (n+1))//2

    return fuel_cost

# 1
print(move_crabs(test, int(median(test))))
print(move_crabs(real, int(median(real))))

# 2
# lazy: try all targets between mean and median, take min...
low = int(median(test))
high = int(round(sum(test) / len(test)))
print(min(move_crabs(test, target, False) for target in range(low, high + 1)))
low = int(median(real))
high = int(round(sum(real) / len(real)))
print(min(move_crabs(real, target, False) for target in range(low, high + 1)))
