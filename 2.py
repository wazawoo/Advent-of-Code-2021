test_raw = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""

test = list(test_raw.splitlines())
real = list(open("2.txt").read().splitlines())

def get_position(instructions):
    x = 0
    y = 0

    for instr in instructions:
        dir, amt = instr.split()
        amt = int(amt)

        if dir == "forward":
            x += amt
        elif dir == "down":
            y -= amt
        elif dir == "up":
            y += amt

    return x * -y

def get_aim(instructions):
    x = 0
    y = 0
    aim = 0

    for instr in instructions:
        dir, amt = instr.split()
        amt = int(amt)

        if dir == "forward":
            x += amt
            y += aim * amt
        elif dir == "down":
            aim -= amt
        elif dir == "up":
            aim += amt

    return x * -y

# 1
print(get_position(test))
print(get_position(real))

# 2
print(get_aim(test))
print(get_aim(real))
