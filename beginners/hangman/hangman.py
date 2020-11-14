from string import ascii_lowercase

from gallows import HANGMAN_GALLOWS
from word import get_random_word

RANDOM_WORD = get_random_word()

def display_board(wrong_answers, idxs):
    print(HANGMAN_GALLOWS[len(wrong_answers)], end='\t')

    curr_ans = ''.join([' ' +letter+ ' ' if idxs[i] else '__ ' for i, letter in enumerate(RANDOM_WORD)])
    print(curr_ans.strip())
    print()

def player_input(remaining_letters):
    while True:
        guessed_letter = input("Pick a letter. Choose wisely: ").lower()
        if (len(guessed_letter) != 1) or (guessed_letter not in ascii_lowercase):
            print(f"{guessed_letter} is not a valid letter.")
        elif guessed_letter not in remaining_letters:
            print(f"You already picked {guessed_letter}.")
        else:
            remaining_letters.remove(guessed_letter)
            return guessed_letter

def win_condition(wrong_answers, idxs, remaining_letters, win_cond):
    while len(wrong_answers) < 6:
        guessed_letter = player_input(remaining_letters)
        if guessed_letter in RANDOM_WORD:
            for i in range(len(RANDOM_WORD)):
                if guessed_letter == RANDOM_WORD[i]:
                    idxs[i] = True
                    display_board(wrong_answers, idxs)
        else:
            wrong_answers.append(guessed_letter)
            display_board(wrong_answers, idxs)
        if False not in idxs:
            win_cond = True
            return win_cond
    return win_cond

def hangman_game():
    # Initialize state variables
    wrong_answers = []
    idxs = [letter not in ascii_lowercase for letter in RANDOM_WORD]
    remaining_letters = set(ascii_lowercase)
    win_cond = False

    print("Welcome to a game of hangman where you have 5 chances to win the game.")
    display_board(wrong_answers, idxs)
    win_condition(wrong_answers, idxs, remaining_letters, win_cond)

if __name__ == '__main__':
    while hangman_game():
        print()
