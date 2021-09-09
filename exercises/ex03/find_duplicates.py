"""Finding duplicate letters in a word."""

__author__ = "730444340"

word: str = input("Enter an word: ")
i: int = 0
flag: bool = False
while i < len(word) and flag is False:
    j: int = i + 1
    while j < len(word) and flag is False:
        if word[j] == word[i]:
            flag = True
        j = j + 1
    i = i + 1
print("Found duplicate: " + str(flag))
