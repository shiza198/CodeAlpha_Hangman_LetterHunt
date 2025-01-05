import random

def LetterHunt():
    # Categorized word lists with hints
    categories = {
        "Fruits": [
            "apple", "banana", "grape", "orange", "mango", "papaya", "pineapple", "kiwi", "watermelon", 
            "strawberry", "blueberry", "peach", "cherry", "pomegranate", "apricot"],
        "Animals": ["elephant", "tiger", "giraffe", "kangaroo", "penguin", "dolphin", "lion", "zebra",
                    "cheetah", "scorpion", "octopus", "squirrel", "turtle", "flamingo", "peacock"],
        "Countries": ["canada", "brazil", "japan", "india", "germany", "australia", "france", "italy", 
                      "china", "mexico", "egypt", "argentina", "russia", "spain", "norway"],
        "Colors": ["red", "blue", "green", "yellow", "purple", "orange", "pink", "black", "white", 
                   "brown", "violet", "cyan", "magenta", "silver", "indigo"]
    }
    
    score = 0  # Initialize score outside the loop to retain across rounds

    while True:
        # Choose a random category and word
        category, words = random.choice(list(categories.items()))
        word_to_guess = random.choice(words)
        guessed_word = ["_"] * len(word_to_guess)
        guessed_letters = set()
        attempts_remaining = 6

        print("\t\t\t\t\t\tWelcome to Letter Hunt\t\t\t\t\t\t")
        print(f"\nYou have {attempts_remaining} attempts to Guess the Word")
        print(f"Hint: The Letter you have to Guess belongs to the {category} Category")
        print("Score:", score)  # Display the current score
        
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
                    score += 10  # Increment the score for a correctly guessed word
                    print("Score:", score)
                    while True:
                        print("Press 1 for Next Word \nPress 2 for Exit")
                        choice = input("Enter your choice: ").strip()
                        if choice == "1":
                            break  # Start a new round
                        elif choice == "2":
                            print("Thanks for playing! Goodbye!")
                            return
                        else:
                            print("Invalid choice. Please enter 1 or 2.")
                    break

            else:
                print("Wrong guess.")
                attempts_remaining -= 1

        if attempts_remaining == 0:
            print("\nYou've run out of attempts. The word was:", word_to_guess)
            while True:
                print("Press 1 for Next Word \nPress 2 for Exit")
                choice = input("Enter your choice: ").strip()
                if choice == "1":
                    break  # Start a new round
                elif choice == "2":
                    print("Thanks for playing! \nGoodbye!")
                    return
                else:
                    print("Invalid choice. Please enter 1 or 2.")

LetterHunt()
