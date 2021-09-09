"""Drawing forests in a loop."""

__author__ = "730444340"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
depth: int = int(input("Enter Depth: "))
i: int = 1
while i <= depth:
    j: int = 1
    line: str = ""
    while j <= i:
        line = line + TREE
        j = j + 1
    print(line)
    i = i + 1
