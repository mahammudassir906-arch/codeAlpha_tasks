# Task 1 - Hangman Game
import random

words = ["python", "engineering", "signals", "coding", "telecommunication"]


def hangman():
    word = random.choice(words)
    guessed = []
    attempts = 6

    print("\n🎮 Welcome to Hangman!")
    print("_ " * len(word))

    while attempts > 0:
        display = " ".join([letter if letter in guessed else "_" for letter in word])
        print(f"\nWord: {display}")
        print(f"Attempts left: {attempts}")
        print(f"Guessed letters: {', '.join(guessed) if guessed else 'None'}")

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter a single letter!")
            continue

        if guess in guessed:
            print("⚠️ Already guessed that letter!")
            continue

        guessed.append(guess)

        if guess in word:
            print("✅ Correct!")
            if all(letter in guessed for letter in word):
                print(f"\n🎉 You Win! The word was: {word}")
                return
        else:
            attempts -= 1
            print(f"❌ Wrong! {attempts} attempts remaining.")

    print(f"\n💀 Game Over! The word was: {word}")

while True:
    hangman()
    play_again = input("\nPlay again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! 👋")
        break
