import random

# these are variables
file = open('words.txt', 'r')
words = file.readlines()
guess_list = []

selected_word = ''

# this is a function
def select_word():
    selected_word = random.choice(words)
    if len(selected_word) > 6:
        select_word()

def guess_input():
    guess = input("Choose a letter: ").lower()
    if len(guess) != 1:
        print("You may only guess 1 letter at a time")
    else:
        guess_list.append(guess)

def display_word():
    for char in selected_word:
        if char in guess_list:
            print(char)
        else:
            print("_")

    print([letter if letter in guess_list else '_' for letter in selected_word])

def guess():
    # appending to guess list
    guess_input()
    display_word()

select_word()
print(len(selected_word))

guess()
guess()
