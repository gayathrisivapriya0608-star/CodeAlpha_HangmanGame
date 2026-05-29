import random

# List of .predefined words
words = ["python", "logic", "puzzle", "system", "coding"]

# Randomly choose a word
target_word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of attempts
attempts_left = 6

print("---- Welcome to Hangman! ----")

# Main game loop
while attempts_left > 0:

    # Display current progress
    display_word = ""

    for letter in target_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Attempts left:", attempts_left)
    print("Guessed letters:", guessed_letters)

    # Check if player won
    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word!")
        break

    # Ask user for input
    guess = input("Guess a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.")
        continue

    # Check repeated guess
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Add guessed letter
    guessed_letters.append(guess)

    # Wrong guess handling
    if guess not in target_word:
        attempts_left -= 1
        print("❌ Wrong guess!")

# If attempts become 0
if attempts_left == 0:
    print("\n💀 Game Over!")
    print("The word was:", target_word)