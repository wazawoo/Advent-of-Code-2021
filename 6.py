#!/usr/local/bin/python3

test_raw = """3,4,3,1,2"""

test = list(list(map(int, test_raw.split(","))))
real = list(list(map(int, open("6.txt").read().split(","))))

def simulate_n_days(lanterns, n):

    # convert to dictionary
    lantern_dict = {n: 0 for n in range(9)}
    for lantern in lanterns:
        lantern_dict[lantern] += 1

    for day in range(n):
        lantern_dict = simulate_day(lantern_dict)

    lantern_count = 0
    for lantern in lantern_dict:
        lantern_count += lantern_dict[lantern]

    return lantern_count

def simulate_day(lantern_dict):

    new_dict = lantern_dict.copy()

    for i in range(9):
        new_dict[i] -= lantern_dict[i]
        if i == 0:
            new_dict[6] += lantern_dict[i]
            new_dict[8] += lantern_dict[i]
        else:
            new_dict[i-1] += lantern_dict[i]

    return new_dict

# 1
print(simulate_n_days(test, 80))
print(simulate_n_days(real, 80))

# 2
print(simulate_n_days(test, 256))
print(simulate_n_days(real, 256))
