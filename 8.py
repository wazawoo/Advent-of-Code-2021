#!/usr/local/bin/python3

test_raw = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""

test = list(test_raw.splitlines())
real = list(open("8.txt").read().splitlines())

# segment indices:
#
#   0000
#  5    1
#  5    1
#   6666
#  4    2
#  4    2
#   3333
#
# digits:
#
# 0: 012345 (all but 6)
# 1: 12
# 2: 01346
# 3: 01236
# 4: 1256
# 5: 02356
# 6: 023456 (all but 1)
# 7: 012
# 8: 0123456
# 9: 012356 (all but 4)

# _1_ is only with 2
# _7_ is only with 3
# _4_ is only with 4
# _8_ is only with all 7
# 4 is subset of _9_, vs other 6 segs
# 1 is subset of _3_, vs other 5 segs
# len(_0_ - 7) == 3, vs other 6 segs
# _6_ is the last 6 seg
# len(_5_ - 9) == 0, vs other 5 segs
# _2_ is the last 5 seg

def get_total(lines):
    total = 0
    for line in lines:
        total += get_digits(line)
    return total

def get_digits(line):
    digits = [set()] * 10
    seg_sets = [set(seg) for seg in line.split(" | ")[0].split()]

    # 1 is only with 2 segments, 7 with 3, 4 with 4, 8 with 7
    digits[1] = list(filter(lambda x: len(x) == 2, seg_sets))[0]
    digits[7] = list(filter(lambda x: len(x) == 3, seg_sets))[0]
    digits[4] = list(filter(lambda x: len(x) == 4, seg_sets))[0]
    digits[8] = list(filter(lambda x: len(x) == 7, seg_sets))[0]
    seg_sets.remove(digits[1])
    seg_sets.remove(digits[7])
    seg_sets.remove(digits[4])
    seg_sets.remove(digits[8])

    # 4 is subset of _9_, vs other 6 segs
    digits[9] = list(filter(lambda x: len(x) == 6 and digits[4].issubset(x), seg_sets))[0]
    seg_sets.remove(digits[9])

    # len(_0_ - 7) == 3, vs other 6 segs
    digits[0] = list(filter(lambda x: len(x) == 6 and len(x - digits[7]) == 3, seg_sets))[0]
    seg_sets.remove(digits[0])

    # _6_ is the last 6 seg
    digits[6] = list(filter(lambda x: len(x) == 6, seg_sets))[0]
    seg_sets.remove(digits[6])

    # 1 is subset of _3_, vs other 5 segs
    digits[3] = list(filter(lambda x: len(x) == 5 and digits[1].issubset(x), seg_sets))[0]
    seg_sets.remove(digits[3])

    # len(_5_ - 9) == 0, vs other 5 segs
    digits[5] = list(filter(lambda x: len(x) == 5 and len(x - digits[9]) == 0, seg_sets))[0]
    seg_sets.remove(digits[5])

    # _2_ is the last 5 seg
    digits[2] = list(filter(lambda x: len(x) == 5, seg_sets))[0]
    seg_sets.remove(digits[2])

    # we have all digits now...

    out_digits = [set(dig) for dig in line.split(" | ")[1].split()]
    out = ""

    for dig in out_digits:
        out += str(digits.index(dig))

    return int(out)

def count_1478(lines):
    num_1478 = 0

    lengths = [2, 3, 4, 7]

    for line in lines:
        digits = line.split(" | ")[1].split()
        for digit in digits:
            if len(digit) in lengths:
                num_1478 += 1

    return num_1478

# 1
print(count_1478(test))
print(count_1478(real))

# 2
print(get_total(test))
print(get_total(real))
