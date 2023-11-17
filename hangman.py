import random

# Greeting
name = input("What is your name?\n")
print ("Hello {}, Welcome to Hangman!".format(name))

# Define list of words
words = ["charm", "pretty", "obstacle", "difficulty", "speaker", "Peru", "sun", "vitamins", "fan", "glasses"]

# Randomize word and output length
word = random.choice(words)
print ("Your word has {} letters".format(len(word)))

wordGuessed = [ "_" for i in len(word)]
print(wordGuessed)

