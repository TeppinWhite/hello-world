import csv
import random

word_to_guess = []
word_to_show = []
word_blank_to_compare = []
letter_guesses = []
animal_list = []
guess_counter = 0

print('Welcome to hangman!')
print('Try to guess the word one letter at a time')
print('If you guess wrong 8 times, you\'re hung')
print('All words are an animal name')


def choose_word():
    global word
    with open(r'C:\Users\User\Desktop\Python\AnimalList.csv') as animal:
        reader = csv.reader(animal)
        for row in reader:
            animal_list.append(row)

    sublist = random.choice(animal_list)
    word = sublist[0]
    word = word.lower()


def guess_word_create():
    for wordlst in word:
        for letter in wordlst:
            word_to_guess.append(letter)
            word_to_show.append('_')
            word_blank_to_compare.append('_')


def guess_letter():
    print('Letters Guessed')
    print(sorted(letter_guesses))
    print(word_to_show)
    global guess
    guess = input('What letter do you guess?\n')


def check_letter():
    letter_guesses.append(guess)
    if guess in word_to_guess:
        letter_check = word_to_guess.count(guess)
        for check in range(letter_check):
            lett = word_to_guess.index(guess)
            word_to_guess[lett] = '_'
            word_to_show[lett] = guess
    else:
        print('That letter is not in the word.')
        global guess_counter
        guess_counter += 1


def win_lose_condition():
    if guess_counter >= 8:
        print('You lose!')
        print('The word was ' + word + '.')

    elif word_to_guess == word_blank_to_compare:
        print('You Win!!!')
        print('The word was ' + word + '.')


def clear_lists():
    word_to_guess.clear()
    word_to_show.clear()
    word_blank_to_compare.clear()
    letter_guesses.clear()
    global guess_counter
    guess_counter = 0


def main():
    while True:
        choose_word()
        guess_word_create()
        while guess_counter <= 8 and word_to_guess != word_blank_to_compare:
            guess_letter()
            check_letter()
        win_lose_condition()
        clear_lists()


if __name__ == '__main__':
    main()

