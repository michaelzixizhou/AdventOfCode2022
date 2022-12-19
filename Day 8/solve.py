def solve():
    # dont account for outer edges
    valid = []
    count = 0
    highestscore = 0
    for y in range(1, len(lines) - 1):
        for x in range(1, len(lines[0]) - 1):
            helper = checkDirections(int(lines[y][x]), x, y)
            if helper[0]:
                count += 1
                valid.append((x, y))
            if helper[1] > highestscore:
                highestscore = helper[1]

    # account for outer edges
    count += 2*len(lines) + 2*len(lines[0]) - 4
    print(count)
    print(highestscore)

def checkDirections(curr: int, x: int, y: int):
    visiblity = [True, True, True, True]
    # scenic score
    score = [0, 0, 0, 0]
    for up in range(y - 1, -1, -1):
        score[0] += 1
        if curr <= int(lines[up][x]):
            visiblity[0] = False
            break
    for down in range(y + 1, len(lines)):
        score[1] += 1
        if curr <= int(lines[down][x]):
            visiblity[1] = False
            break
    for left in range(x - 1, -1, -1):
        score[2] += 1
        if curr <= int(lines[y][left]):
            visiblity[2] = False
            break
    for right in range(x + 1, len(lines[0])):
        score[3] += 1
        if curr <= int(lines[y][right]):
            visiblity[3] = False
            break
    
    # calculate score
    totalscore = 1
    for i in score:
        totalscore *= i

    return (any(visiblity), totalscore)



if __name__ == "__main__":
    with open("Day 8/day8input.txt", "r") as data: 
        lines = data.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].strip()
    solve()