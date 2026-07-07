import random
import string

# ==========================================
#        HANGMAN GAME - CodeAlpha
# ==========================================

WORDS = {
    "Programming": [
        "python", "variable", "function", "compiler", "debugger",
        "integer", "boolean", "operator", "library", "package"
    ],
    "Fruits": [
        "apple", "banana", "orange", "mango", "grapes",
        "papaya", "pineapple", "watermelon", "guava", "peach"
    ],
    "Animals": [
        "elephant", "tiger", "lion", "rabbit", "monkey",
        "giraffe", "zebra", "kangaroo", "penguin", "dolphin"
    ]
}


def choose_word():
    category = random.choice(list(WORDS.keys()))
    word = random.choice(WORDS[category])
    return category, word


def display_word(secret_word, guessed_letters):
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter.upper() + " "
        else:
            display += "_ "
    return display.strip()


def validate_input(letter):
    if len(letter) != 1:
        return False
    if letter not in string.ascii_letters:
        return False
    return True


def calculate_accuracy(correct, wrong):
    total = correct + wrong
    if total == 0:
        return 0
    return round((correct / total) * 100, 2)


def play_game():

    category, secret_word = choose_word()

    guessed_letters = []
    wrong_letters = []

    correct_guesses = 0
    wrong_guesses = 0
    max_attempts = 6

    print("\n" + "=" * 45)
    print("🎮       HANGMAN GAME")
    print("=" * 45)

    print(f"\nCategory : {category}")

    while True:

        print("\n" + "-" * 45)

        print("Word :", display_word(secret_word, guessed_letters))

        print(f"Wrong Attempts : {wrong_guesses}/{max_attempts}")

        print("Used Letters :", " ".join(sorted(guessed_letters)) if guessed_letters else "None")

        print("-" * 45)

        guess = input("Enter a Letter : ").lower().strip()

        if not validate_input(guess):
            print("❌ Invalid Input! Enter only ONE alphabet.")
            continue

        if guess in guessed_letters:
            print("⚠ You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:

            print("✅ Correct Guess!")

            correct_guesses += 1

        else:

            print("❌ Wrong Guess!")

            wrong_letters.append(guess)

            wrong_guesses += 1

        if all(letter in guessed_letters for letter in secret_word):

            print("\n🎉 Congratulations!")
            print(f"You guessed the word : {secret_word.upper()}")

            accuracy = calculate_accuracy(correct_guesses, wrong_guesses)

            print("\n========== GAME SUMMARY ==========")
            print("Result            : WIN")
            print("Correct Guesses   :", correct_guesses)
            print("Wrong Guesses     :", wrong_guesses)
            print("Accuracy          :", accuracy, "%")
            print("==================================")

            break

        if wrong_guesses == max_attempts:

            print("\n💀 GAME OVER!")
            print(f"The correct word was : {secret_word.upper()}")

            accuracy = calculate_accuracy(correct_guesses, wrong_guesses)

            print("\n========== GAME SUMMARY ==========")
            print("Result            : LOSE")
            print("Correct Guesses   :", correct_guesses)
            print("Wrong Guesses     :", wrong_guesses)
            print("Accuracy          :", accuracy, "%")
            print("==================================")

            break


while True:

    play_game()

    choice = input("\nDo you want to play again? (Y/N): ").upper()

    if choice != "Y":
        print("\n👋 Thank you for playing Hangman!")
        break