"""Repeating a beat in a loop."""

__author__ = "730444340"


# Begin your solution here...

beat: str = input("What beat do you want to repeat? ")
times: int = int(input("How many times do you want to repeat it? "))
result: str = ""
if times <= 0:
    print("No beat...")
else:
    i: int = 0
    while i < times - 1:
        result = result + beat + " "
        i = i + 1
result = result + beat
print(result)