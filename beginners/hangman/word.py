import random

WORDLIST = 'wordlist.txt'

def get_random_word():
    """Generate a random word from wordlist.txt using reservoir sampling."""
    words_counter = 0
    curr_word = None
    with open(WORDLIST, 'r') as f:
        for word in f:
            if '(' in word or ')' in word:
                continue
            word = word.strip().lower()
            if len(word) > 6:
                continue
            words_counter += 1
            if random.randint(1, words_counter) == 1:
                curr_word = word
        return curr_word 