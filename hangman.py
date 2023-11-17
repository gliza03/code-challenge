import random

# Greeting
name = input("What is your name?\n")
print ("Hello {}, Welcome to Hangman!".format(name))

# Define list of words
words = ["charm", "pretty", "obstacle", "difficulty", "speaker", "Peru", "sun", "vitamins", "fan", "glasses"]

def hangman():
    # Randomize word and output length
    word = random.choice(words)
    print ("Your word has {} letters".format(len(word)))

    wordGuessed = [ "_" for i in range(len(word))]

    guesses = 0
    incorrectGuesses = 0
    correctGuesses = 0
    index = 0
    lettersUsed = []

    while index < len(wordGuessed):
        letter = input("Guess a letter:\n")
        if letter not in lettersUsed:
            lettersUsed.append(letter)
            guesses += 1
            if letter not in word:
                incorrectGuesses+=1
                print("Sorry! That letter is not in the word.\n")
            
            for let, num in enumerate(word):
                if num == letter:
                    wordGuessed[let] = letter
                    correctGuesses += 1
                    index+=1
        else:
            print("You already used that letter!")
        
        print(wordGuessed)
        print("Number of guesses: {} (Correct: {} | Incorrect: {})".format(guesses,correctGuesses,incorrectGuesses))
        
    print("You guessed right!\n")
    print("Number of guesses: {} (Correct: {} | Incorrect: {})".format(guesses,correctGuesses,incorrectGuesses))

    decision = input("Do you want to play again? Type Y for yes and N for no.")
    if decision == "Y":
        hangman()
    exit()

hangman()