import random

# Greeting
name = input("What is your name?\n")
print ("Hello {}, Welcome to Hangman!".format(name))

# Define list of words
words = ["charm", "pretty", "obstacle", "difficulty", "speaker", "Peru", "sun", "vitamins", "fan", "glasses"]

# Randomize word and output length
word = random.choice(words)
print ("Your word has {} letters".format(len(word)))

wordGuessed = [ "_" for i in range(len(word))]

guesses = 0
incorrectGuesses = 0
correctGuesses = 0

while index < len(wordGuessed):
    letter = input("Guess a letter:")
    guesses += 1
    for let, num in enumerate(word):
        if let == letter:
            wordGuessed[num] = letter
            correctGuesses += 1
            index+=1
        else:
            print("This letter is not in the word. Try again!")
            incorrectGuesses +=1
    print(wordGuessed)
    print("Number of guesses: {} (Correct: {} | Incorrect: {})".format(guesses,correctGuesses,incorrectGuesses))
    
print("You guessed right!")

