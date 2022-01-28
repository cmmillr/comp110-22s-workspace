"""One-Shot Wordle with Loops."""

__author__ = "730317751"
# python -m exercises.ex02_one_shot_wordle
secret_word: str = "python"
guess_word: str = input("What is your 6-letter guess? ")
guess_index: int = 0

guess_block: str = ""

white_box: str = " \U00002B1C"
green_box: str = " \U0001F7E9"
yellow_box: str = " \U0001F7E8"

while guess_index < 6:
    if guess_word[guess_index] == secret_word[guess_index]:
        guess_block = guess_block + green_box
    else:
        guess_block = guess_block + white_box
    guess_index = guess_index + 1
print(guess_block)
while len(guess_word) != 6:
    guess_word: str = input("That was not 6 letters! Try again: ")
if len(guess_word) == 6:
    if guess_word == "python":
        print("Woo! You got it!")
    else:
        print("Not quite. Play again soon!")

