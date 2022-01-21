"""ex01 - Chardle - A cute step toward Wordle."""

__author__ = "730317751"

word: str = input("Enter a 5-character word: ")
character: str = input("Enter a single character: ")
matches: int = (0)
print("Searching for", character, "in", word)
if word[0] == character:
    print(character, "found at index 0")
    matches = matches + 1
if word[1] == character:
    print(character, "found at index 1")
    matches = matches + 1
if word[2] == character:
    print(character, "found at index 2")
    matches = matches + 1
if word[3] == character:
    print(character, "found at index 3")
    matches = matches + 1
if word[4] == character:
    print(character, "found at index 4")
    matches = matches + 1

if matches == 0:
    print("No instances of", character, "found in", word)
else:
    if matches == 1:
        print(matches, "instance of", character, "found in", word)
    else:
        print(matches, "instances of", character, "found in", word)
