import random

# List of predefined words
words = ["python", "apple", "robot", "music", "water"]

# Randomly choose a word
secret_word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Maximum wrong guesses
wrong_guesses = 0
max_wrong_guesses = 6

print("===================================")
print("🎮 Welcome to Hangman Game!")
print("===================================")

while wrong_guesses < max_wrong_guesses:

    display_word = ""

    # Build the displayed word
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if player has guessed the word
    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word!")
        break

    guess = input("Enter a letter: ").lower()

    # Check if already guessed
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Correct Guess!")
    else:
        wrong_guesses += 1
        print("❌ Wrong Guess!")
        print("Remaining Chances:", max_wrong_guesses - wrong_guesses)

else:
    print("\n💀 Game Over!")
    print("The correct word was:", secret_word)