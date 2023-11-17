import random

# Greeting
name = input("What is your name?\n")
print ("Hello {}, Welcome to Hangman!".format(name))

# Define list of words
words = ["charm", "pretty", "obstacle", "difficulty", "speaker", "prey", "sun", "vitamins", "fan", "glasses"]

def hangman():
    # Randomize word and output length
    word = random.choice(words)
    print ("Your word has {} letters".format(len(word)))

    wordGuessed = [ "_" for i in range(len(word))]

    # Define variables
    guesses = 0
    incorrectGuesses = 0
    correctGuesses = 0
    index = 0
    lettersUsed = []

    while index < len(wordGuessed):
        letter = input("Guess a letter:\n").lower()

        # Eliminate invalid entries, such as numbers
        if len(letter)!=1 or letter.isdigit():
            print("Invalid entry!")
            continue
        if not isinstance(letter,str):
            print("Invalid entry!")
            continue
        
        # If the letter was used, do not run the code
        if letter not in lettersUsed:
            lettersUsed.append(letter)
            guesses += 1
            # Incorrect
            if letter not in word:
                incorrectGuesses+=1
                print("\nSorry! {} is not in the word.".format(letter))
            
            # Correct
            for let, num in enumerate(word):
                if num == letter:
                    wordGuessed[let] = letter
                    correctGuesses += 1
                    index+=1
        elif letter in lettersUsed:
            guesses += 1
            print("You already used that letter!\n")
        
        print(wordGuessed)
        print("Number of guesses: {} (Correct: {} | Incorrect: {})\n\n".format(guesses,correctGuesses,incorrectGuesses))
        
    print("You guessed right!")
    print("Number of guesses: {} (Correct: {} | Incorrect: {})\n\n".format(guesses,correctGuesses,incorrectGuesses))

    decision = input("Do you want to play again? Type Y for yes, if not, type anything else.\n")
    if decision == "Y":
        hangman()
    exit()

hangman()