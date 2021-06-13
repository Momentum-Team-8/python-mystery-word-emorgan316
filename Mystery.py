import random

# these are variables
file = open('words.txt', 'r')
words = file.read().lower().split()
guess_list = []

selected_word = ''
selected_word_list = selected_word.split()

# this is a function
def select_word():
    selected_word = random.choice(words)
    if selected_word.count > 6:
        select_word()

def play():
    incorrect_guesses = []
    guess_input()
    display_word(guess_list)
    
    if "_" in selected_word:
        print(f"Mystery Word: {' '.join(display_word(selected_word_list, guess_list))}")
        print(f"You've already guessed: {' '.join(incorrect_guesses)}")
        print(f"You have {guesses_available} guesses left")
    elif guesses < 8 and "_" not in selected_word_list:
        print(f"Yay! you guessed the Mystery Word {selected_word}")

def guess_input():
    guess = input("Choose a letter: ").lower()
    if len(guess) != 1:
        print("You may only guess 1 letter at a time")
    else:
        guess_list.append(guess)
    

def display_word(guess_list):
    print([letter if letter in guess_list else '_' for letter in selected_word])

select_word()

play()