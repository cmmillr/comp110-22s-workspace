"""An example of conditional (if-else) statements."""

SECRET: int = 3

print("I'm thinking of a value betweeen 1 and 5. What is it? ")
guess: int = int(input("What is your guess? "))

if guess == SECRET:
    print("You guessed correctly!!!")
    print("Please continue to have a successful day!")
else:
    print("You're wrong. Sux bro.")
    if guess > SECRET:
        print("You guessed too high, dumbass")
    else:
        print("You guessed too low, dumbass")

print("Game Over.")