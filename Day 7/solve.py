all_trees = []

class Tree:
    def __init__(self, name: str) -> None:
        self.name = name
        self.size = 0
        self.parent = None
        self.subtree = []
        all_trees.append(self)

    def __repr__(self) -> str:
        return self.name
    
    def __str__(self,level=0):
        ret = " " * level + "dir " + str(self.name) + " " + str(self.size) + '\n'
        for child in self.subtree:
            ret += child.__str__(level+1)

        return ret

def make_tree():
    curr = head = Tree("/")

    for i in lines:
        char = i[:4]
        if char == "$ cd":
            curr = cdHelper(head, curr, i[5:])
        elif char == "$ ls":
            pass
        elif char == "dir ":
            temp = Tree(i[4:].strip())
            temp.parent = curr
            curr.subtree.append(temp)
        else:
            temp = ''.join(c for c in i[:] if c.isdigit())
            curr.size += int(temp)
    
    add_sizes(head)

    return head


def cdHelper(head:Tree, curr: Tree, command: str):
    command = command.strip()
    if command == "..":
        return curr.parent if curr.parent else head
    elif command == "/":
        return head
    else:
        for i in curr.subtree:
            if i.name == command:
                return i
        return curr


def add_sizes(tree: Tree):
    for i in tree.subtree:
        add_sizes(i)
        tree.size += i.size


def solvept1(head: Tree, limit: int):
    count = 0
    total = head.size
    for i in all_trees:
        if i.size <= limit:
            count += i.size
    print("Under " + str(limit) + ": " + str(count))
    print("Total: " + str(total))


def solvept2(head: Tree, unuseddiskspace: int, totaldiskspace: int):
    smallest = total = head.size
    for i in all_trees[1:]:
        curr = total - i.size
        if curr <= totaldiskspace - unuseddiskspace and i.size < smallest:
            smallest = i.size   

    print("Smallest deletable dir: " + str(smallest))



if __name__ == "__main__":
    with open("Day 7/day7input.txt", "r") as data: 
        lines = data.readlines()
    tree = make_tree()
    solvept1(tree, 100_000)
    solvept2(tree, 30_000_000, 70_000_000)