def solve() -> int:
    most = second = third = curr = 0
    for line in data:
        # separate by newline
        if line == '\n':
            curr = 0
        else:
            curr += int(line[:-1])

        # top 3 placement
        if curr > most:
            most, second, third = curr, most, second
        elif curr > second:
            second, third = curr, second
        elif curr > third:
            third = curr
        
    return most+ second+ third


if __name__ == "__main__":
    data = open('Day 1/day1input.txt', 'r').readlines()
    print(solve())