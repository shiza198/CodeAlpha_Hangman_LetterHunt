import random

def hangman():
    # List of words for the game
    words = ["python", "hangman", "programming", "developer", "challenge", "algorithm"]
    word_to_guess = random.choice(words)
    guessed_word = ["_"] * len(word_to_guess)
    guessed_letters = set()
    attempts_remaining = 6

    print("Welcome to Hangman!")
    print("You have", attempts_remaining, "attempts to guess the word.")

    while attempts_remaining > 0:
        print("\nWord: ", " ".join(guessed_word))
        print("Guessed letters: ", " ".join(sorted(guessed_letters)))
        print("Attempts remaining:", attempts_remaining)

        guess = input("Enter a letter: ").lower()

        # Check for valid input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word_to_guess:
            print("Good guess!")
            for i, letter in enumerate(word_to_guess):
                if letter == guess:
                    guessed_word[i] = guess

            if "_" not in guessed_word:
                print("\nCongratulations! You've guessed the word:", word_to_guess)
                break
        else:
            print("Wrong guess.")
            attempts_remaining -= 1

    if attempts_remaining == 0:
        print("\nYou've run out of attempts. The word was:", word_to_guess)

if __name__ == "__main__":
    hangman()
