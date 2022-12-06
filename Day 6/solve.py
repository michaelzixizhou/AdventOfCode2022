def solve(r: int):
    s = lines[0]
    for i in range(len(s)):
        string = ""
        for j in range(r):
            string += s[i+j]
        if len(set(string)) == r:
            return i + r
    

if __name__ == "__main__":
    with open("Day 6/day6input.txt", "r") as data: 
        lines = data.readlines()
    print(solve(14))