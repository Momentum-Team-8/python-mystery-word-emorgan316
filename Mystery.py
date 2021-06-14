import random

# these are variables
file = open('words.txt', 'r')
words = file.read().splitlines()
guess_list = []
guess_count = 0

selected_word = ''

# this is a function
def select_word():
    selected_word = random.choice(words)
    # print(selected_word)
    # print(len(selected_word)) 
    if len(selected_word) > 6:
        return select_word()
    print(selected_word)
    return selected_word
    

def guess_input():
    guess = input("Choose a letter: ").lower()
    if len(guess) != 1:
        print("You may only guess 1 letter at a time")
    else:
        guess_list.append(guess)

def display_word(selected_word):
    for char in selected_word:
        if char in guess_list:
            print(char, end = '')
        else:
            print("_", end = '')
    print("")

def guess(selected_word):
    # appending to guess list
    guess_input()
    display_word(selected_word)

def game_over(selected_word):
    for char in selected_word:
        if char not in guess_list:
            return False
    return True

selected_word = select_word()
# print(len(selected_word))

while not game_over(selected_word):
    guess(selected_word)
    guess_count = guess_count + 1
    if guess_count == 6:
        break



