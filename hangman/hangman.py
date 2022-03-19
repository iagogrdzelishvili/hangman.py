import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()
def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 9
    lives = 10

    while len(word_letters) > 0 and lives > 0:
        print('შენ გაქვს', lives, 'სიცოცხლე დარჩენილი, გამოიცანი ასო ან სიტყვა: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('შენი სიტყვაა: ', ' '.join(word_list))

        user_letter = input('გამოიცანი ასო: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
            else:
                lives = lives - 1
                print('\nარჩეული ასო,', user_letter, 'არ არის სიტყვაში.')
        elif user_letter in used_letters:
            print('\nშენ უკვე გამოყენებული გაქვს ეს ასო, კიდევ სცადე.')
        else:
            print('\nარ არის სწორი ასო.')

    if lives == 0:
        print('შენ დამარცხდი, სიტყვა იყო:', word)
    else:
        print('გილოცავ! შენ გაიმარჯვე, სიტყვა არის:', word, '!!')
if __name__ == '__main__':
    hangman()
