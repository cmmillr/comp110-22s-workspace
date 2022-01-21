"""Quiz practice"""

choice: int = int(input("Pick a number. "))

if choice < 50:
    if choice < 25:
        print("A")
    else:
        print("B")
else:
    if choice > 75:
        print("C")
    else:
        print("D")