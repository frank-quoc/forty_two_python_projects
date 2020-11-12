from word import get_random_word
from gallow import HANGMAN_GALLOWS
from string import ascii_lowercase

RANDOM_WORD = get_random_word()

def welcome_msg():
    print("WELCOME TO HANGMAN!")
    print("You have 6 chances before you lose the game. Choose wisely.")

def display_board(wrong_letters, correct_letters, random_word):
    print(GALLOWS[len(wrong_letters)])
    print()

    print("Missed letters:", " ".join(wrong_letters))
    print()

    blanks = "_ "*len(random_word) 
    for i in range(len(random_word)):
        if random_word[i] in ran


if __name__ == '__main__':
