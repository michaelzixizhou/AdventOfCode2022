def solve():
    total = 0
    for i in data:
        # total += points(i[2])
        total += matchup(i[2], i[0])
    return total 
        

def points(a):
    if a == "X":
        return 1
    elif a == "Y":
        return 2
    elif a == "Z":
        return 3


def matchup(b, a):
    # rock
    if a == "A":
        if b == "X":
            return 0 + 3
        elif b == "Y":
            return 3 + 1
        elif b == "Z":
            return 6 + 2
    # paper
    if a == "B":
        if b == "X":
            return 0 + 1
        elif b == "Y":
            return 3 + 2
        elif b == "Z":
            return 6 + 3

    # scissors
    if a == "C":
        if b == "X":
            return 0 + 2
        elif b == "Y":
            return 3 + 3
        elif b == "Z":
            return 6 + 1

    
if __name__ == "__main__":
    data = open("Day 2/day2input.txt", "r").readlines()
    print(solve())