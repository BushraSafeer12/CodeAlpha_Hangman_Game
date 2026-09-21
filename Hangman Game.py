import random
words = ['python', 'chicken', 'ali', 'play', 'fork']
secret_word = random.choice(words)
guessed_letters = []
incorrect_guesses = 0
max_guesses = 6
print("------------ Welcome to the Hangman Game -----------")
display_word = ""
for letter in secret_word:
    display_word += "_"
print("Word:", display_word)
while True:
    guess = input("Enter a guess: ").lower()
    if len(guess) != 1:
        print("Please enter only one letter.")
        continue
    if guess in guessed_letters:
        print("You already guessed this letter")
    else:
        guessed_letters.append(guess)

        if guess in secret_word:
            print("You guessed this letter")
        else:
            print("Wrong guess. Try Again")
            incorrect_guesses += 1

            if incorrect_guesses == max_guesses:
                print("Game Over!")
                break

    word_guessed = True
    display_word = ""

    for letter in secret_word:
        if letter not in guessed_letters:
            word_guessed = False

        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"
    if word_guessed:
        print("You won!")
        break

    print("Word:", display_word)