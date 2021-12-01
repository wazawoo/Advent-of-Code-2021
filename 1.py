test_raw = """199
200
208
210
200
207
240
269
260
263"""

p1_test = list(map(int, test_raw.splitlines()))
p1_real = list(map(int, open("1.txt").read().splitlines()))

def count_increases(depths):
    total = 0

    for (i, depth) in enumerate(depths):
        if i == 0:
            continue
        if depth > depths[i-1]:
            total += 1

    return total


def count_group_increases(depths):
    total = 0
    last_sum = 0

    for (i, depth) in enumerate(depths):
        if i > len(depths) - 3:
            continue

        window_sum = sum(depths[i:i+3])

        if i > 0 and window_sum - last_sum > 0:
            total += 1

        last_sum = window_sum

    return total


# part 1
print(count_increases(p1_test))
print(count_increases(p1_real))

# part 2
print(count_group_increases(p1_test))
print(count_group_increases(p1_real))
