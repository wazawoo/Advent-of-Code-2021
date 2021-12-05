test_raw = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""

test = list(test_raw.splitlines())
real = list(open("5.txt").read().splitlines())

def find_num_safe_points(lines, include_diagonal):

    dict = {}
    total = 0

    for line in lines:
        p1, p2 = line.split(" -> ")
        x1, y1 = p1.split(",")
        x2, y2 = p2.split(",")
        x1 = int(x1)
        y1 = int(y1)
        x2 = int(x2)
        y2 = int(y2)

        # horizontal
        if x1 == x2:

            dx = 0
            dy = 1
            if y1 > y2:
                dy = -1

        # vertical
        elif y1 == y2:

            dy = 0
            dx = 1
            if x1 > x2:
                dx = -1

        # diagonal
        else:
            if include_diagonal:
                dx = 1
                if x1 > x2:
                    dx = -1

                dy = 1
                if y1 > y2:
                    dy = -1
            else:
                continue

        # loop across lines, incrementing dictionary
        for i in range(max(abs(x1 - x2), abs(y1 - y2)) + 1):
            p = str(x1 + dx*i)+","+str(y1 + dy*i)

            dict[p] = dict.get(p, 0) + 1

            if dict[p] == 2:
                total += 1

    return total

# 1
print(find_num_safe_points(test, False))
print(find_num_safe_points(real, False))

# 2
print(find_num_safe_points(test, True))
print(find_num_safe_points(real, True))
