import random

# Greeting
name = input("What is your name?")
print ("Hello {}, Welcome to Hangman!".format(name))

# Define list of words
words = ["charm", "pretty", "obstacle", "difficulty", "speaker", "Peru", "sun", "vitamins", "fan", "glasses"]

# Randomize word and output length
word = random.choice(words)
print (word)
print (len(word))

