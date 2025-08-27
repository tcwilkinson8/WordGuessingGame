import random

game = "GuessTheFive"

word_bank = []
with open("words.txt") as word_file:
    for line in word_file:
        word_bank.append(line.rstrip().lower())

word_to_guess = random.choice(word_bank)
misplaced_guesses = []
incorrect_guesses = []
max_turns = 5
turns_taken = 0

print("Welcome to Guess The Five!")
print("You have 5 attempts to guess the 5-letter word.")

while turns_taken < max_turns:
    guess = input("Guess a word: ").lower()

    if len(guess)  != len(word_to_guess) or not guess.isalpha():
        print("Please enter a 5-letter word.")
        continue

    index = 0
    for c in guess:
        if c == word_to_guess[index]:
            print(c, end=" ")
            if c in misplaced_guesses:
                misplaced_guesses.remove(c)
        elif c in word_to_guess:
            print("_", end=" ")
            if c not in misplaced_guesses:
                misplaced_guesses.append(c)
        else:
            print("X", end=" ")
            if c not in incorrect_guesses:
                incorrect_guesses.append(c)
        index += 1

        print("\n")
        print( "Misplaced letters: ", misplaced_guesses)
        print( "Incorrect letters: ", incorrect_guesses)
        turns_taken += 1

        if guess == word_to_guess:
            print("Congratulations! You've guessed the word correctly!")
            break
        if turns_taken == max_turns:
            print(f"Sorry, you've used all your attempts. The word was '{word_to_guess}'.")
            break

        print(f"You have {max_turns - turns_taken} attempts left.")