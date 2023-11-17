import random

# Greeting
name = input("What is your name?")
print ("Hello %s, Welcome to Hangman!", name)

# Define list of words
words = ["charm", "pretty", "obstacle", "difficulty", "speaker", "Peru", "sun", "vitamins", "fan", "glasses"]

word = random.choice(words)
print(word)

