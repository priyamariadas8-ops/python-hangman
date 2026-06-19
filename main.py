import random

# List of words
words = ["python", "coding", "developer", "keyboard", "network"]

# Choose random word
word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_chances = 6

print("Welcome to Hangman Game!")

while True:

    # Show word with blanks
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display = display + letter + " "
        else:
            display = display + "_ "

    print("\nWord:", display)
    print("Chances left:", max_chances - wrong_guesses)

    # Check win
    if "_" not in display:
        print("Congratulations! You won.")
        break

    # User input
    guess = input("Enter a letter: ").lower()

    # Check valid input
    if len(guess) != 1:
        print("Enter only one letter.")
        continue

    # Check repeated letter
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check correct or wrong
    if guess in word:
        print("Correct guess!")
    else:
        wrong_guesses = wrong_guesses + 1
        print("Wrong guess!")

    # Check lose
    if wrong_guesses == max_chances:
        print("\nGame Over!")
        print("The word was:", word)
        break