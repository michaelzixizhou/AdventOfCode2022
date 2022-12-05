import re


def lstcreation():
    lst = []
    for i in range(9):
        lst.append([])

    for i in lines[:8]:
        for j in range(9):
            index = 4*j + 1
            if i[index] != " ":
                lst[j].append(i[index])
    
    for i in lst:
        i.reverse()
    return lst


def solve(a):
    for i in lines[10:]:
        bounds = [int(s) for s in re.findall(r'\b\d+\b', i)]
        # pt 1
        # for j in range(bounds[0]):
        #     a[bounds[2] - 1].append(a[bounds[1] - 1].pop())
            
        # pt 2
        temp = []
        for j in range(bounds[0]):
            temp.append(a[bounds[1] - 1].pop())  

        for k in range(bounds[0]):
            a[bounds[2] - 1].append(temp.pop())

    s = ""
    for i in a:
        s += i[-1]
    return s


if __name__ == "__main__":
    with open("Day 5/day5input.txt", "r") as data: 
        lines = data.readlines()
    print(solve(lstcreation()))