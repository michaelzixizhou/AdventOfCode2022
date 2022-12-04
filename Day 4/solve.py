import re

def solvept1():
    count = 0
    for i in lines:
        bounds = [int(s) for s in re.findall(r'\b\d+\b', i)]
        total = len(set(list(range(bounds[0], bounds[1]+ 1)) + list(range(bounds[2], bounds[3] + 1))))
        higher = max(bounds[1] - bounds[0] + 1, bounds[3] - bounds[2] + 1)
        if higher == total:
            count += 1
    print(count)


def solvept2():
    count = 0
    for i in lines:
        bounds = [int(s) for s in re.findall(r'\b\d+\b', i)]
        total = len(set(list(range(bounds[0], bounds[1]+ 1)) + list(range(bounds[2], bounds[3] + 1))))
        if total != len(list(range(bounds[0], bounds[1]+ 1))+ list(range(bounds[2], bounds[3] + 1))):
            count += 1

    print(count)


if __name__ == "__main__":
    with open("Day 4/day4input.txt", "r") as data: 
        lines = data.readlines()
    solvept1(); solvept2()