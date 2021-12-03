test_raw = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""

test = list(test_raw.splitlines())
real = list(open("3.txt").read().splitlines())

def most_common_digit(rows, i, flip = False):
    one_count = len(list(filter(lambda x: x[i] == "1", rows)))

    most_is_one = one_count >= len(rows) - one_count

    if flip:
        return str(int(not most_is_one))
    else:
        return str(int(most_is_one))

def get_power(rows):
    gamma = ""
    epsilon = ""
    for i in range(len(rows[0])):
        gamma += most_common_digit(rows, i)
        epsilon += most_common_digit(rows, i, True)

    return int(gamma, 2) * int(epsilon, 2)

def get_rating(rows, flip = False):
    ratings = rows
    for i in range(len(rows[0])):
        maj = most_common_digit(ratings, i, flip)
        ratings = list(filter(lambda x: x[i] == maj, ratings))
        if len(ratings) == 1:
            return ratings[0]

def get_life_support(rows):

    oxy = get_rating(rows)
    co2 = get_rating(rows, True)

    return int(oxy, 2) * int(co2, 2)

# 1
print(get_power(test))
print(get_power(real))

# 2
print(get_life_support(test))
print(get_life_support(real))
