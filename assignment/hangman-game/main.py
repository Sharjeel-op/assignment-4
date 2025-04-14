import random
import string
from words import words  # Ensure this is a list in words.py

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # Letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # Letters guessed by the user

    lives = 6  # Number of tries

    print("🎉 Welcome to Hangman!")

    while len(word_letters) > 0 and lives > 0:
        print("\nYou have", lives, "lives left.")
        print("Used letters:", ' '.join(sorted(used_letters)))

        # Show current word progress
        word_display = [letter if letter in used_letters else '-' for letter in word]
        print("Current word:", ' '.join(word_display))

        # Get user guess
        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("✅ Good guess!")
            else:
                lives -= 1
                print("❌ That letter is not in the word.")
        elif user_letter in used_letters:
            print("⚠️ You've already guessed that letter.")
        else:
            print("❗ Invalid character. Please enter a letter A-Z.")

    # End of game
    if lives == 0:
        print("\n😢 You died. The word was:", word)
    else:
        print("\n🎉 You guessed the word:", word, "! You win!")

# Start the game
hangman()
