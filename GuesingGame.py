secretWord = input("Please enter a word for somebody to guess")
guess = ""
guessCount = 0
guessLimit = 2
out_of_guesses = False

while guess != secretWord and not out_of_guesses:
    if guessCount <= guessLimit:
        guess = input("Try to guess the secret word, you have 3 tries:  ")
        guessCount += 1
# print("That was wrong, you have guessed " + str(guessCount) + " times.")
    else:
        out_of_guesses = True



if out_of_guesses:
    print("Out of guesses, you lose")
else:
    print("You win!")
