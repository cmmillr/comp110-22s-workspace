"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730317751"

word: str = input("Enter a 5-character word: ")
character: str = input("Enter a single character: ")
print("Searching for", character, "in", word)
if word[0] == character:
    print(character, "found at index 0")
if word[1] == character:
    print(character, "found at index 1")
if word[2] == character:
    print(character, "found at index 2")
if word[3] == character:
    print(character, "found at index 3")
if word[4] == character:
    print(character, "found at index 4")