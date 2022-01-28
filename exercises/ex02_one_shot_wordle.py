"""One-Shot Wordle with Loops."""

__author__ = "730317751"
# python -m exercises.ex02_one_shot_wordle
secret_word: str = "knoll"
guess_word: str = input(f"What is your {len(secret_word)}-letter guess? ")
guess_index: int = 0
guess_block: str = ""

white_box: str = " \U00002B1C"
green_box: str = " \U0001F7E9"
yellow_box: str = " \U0001F7E8"

while len(guess_word) != len(secret_word):
    guess_word: str = input(f"That was not {len(secret_word)} letters! Try again: ")
if len(guess_word) == len(secret_word):
    while guess_index < len(secret_word):
        if guess_word[guess_index] == secret_word[guess_index]:
            guess_block = guess_block + green_box
        else:
            somewhere: bool = False
            alt_index: int = 0
            while somewhere is not True and alt_index < len(secret_word):
                if secret_word[alt_index] == guess_word[guess_index]:
                    somewhere = True
                else:
                    alt_index = alt_index + 1
            if somewhere is True:
                guess_block = guess_block + yellow_box
            else:
                guess_block = guess_block + white_box
        guess_index = guess_index + 1
    print(guess_block)
    if guess_word == secret_word:
        print("Woo! You got it!")
    else:
        print("Not quite. Play again soon!")