def solvept1():
    total = 0
    for i in data:
        for j in i[:len(i)//2]:
            if j in i[len(i)//2:]:
                total += priority(j)
                break

    return total

def solvept2():
    total = 0
    i = 0
    while i <= len(data) - 3:
        first, second, third = data[i], data[i+1], data[i+2]
        for j in first:
            if j in second and j in third:
                total += priority(j)
                break
        i += 3

    return total

def priority(a):
    return ord(a) - 96 if ord(a) >= 97 else ord(a) - 38


if __name__ == "__main__":
    data = open("Day 3/day3input.txt", "r").readlines()
    print(solvept1(), solvept2())