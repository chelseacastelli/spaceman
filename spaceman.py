import random
import os
from subprocess import call

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns:
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
        else:
            continue

    return True

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet

    word_with_guesses = []

    for letter in secret_word:
        if letter in letters_guessed:
            word_with_guesses.append(letter)
        else:
            word_with_guesses.append('_')

    return ' '.join(word_with_guesses)


def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    #TODO: check if the letter guess is in the secret word
    if guess in secret_word:
        return True
    else:
        return False

def user_input(prompt):
    user_input = input(prompt)
    return user_input

def clear():
    _ = call('clear' if os.name =='posix' else 'cls')

def start_game():
    print("\nWelcome! Let's play Spaceman :)\nTry guessing the secret word one letter at a time\nbefore the Spaceman is drawn.\nYou get 7 incorrect guesses.. choose wisely.\nGO!\n")

def play_again():
    play_again = user_input("Would you like to play again? (y/n) ")
    if play_again.lower() == 'y':
        clear()
        return True
    clear()
    return False

def spaceman(secret_word, word_with_guesses, letters_guessed, guesses_left):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''

    #TODO: show the player information about the game according to the project spec
    print(f"Guess the {len(secret_word)} letter word\n\n{get_guessed_word(secret_word, letters_guessed)}")

    #TODO: Ask the player to guess one letter per round and check that it is only one letter
    while guesses_left > 0:
        if '_' not in get_guessed_word(secret_word, letters_guessed):
            print("You got it!\n")
            return play_again()

        guess = user_input("\nEnter your guess: ")
        if len(guess) > 1:
            guess = user_input("Input only one letter: ")
        if guess in letters_guessed:
            guess = user_input("You already guessed that letter! Try again: ")
        letters_guessed.append(guess)


        clear()

        #TODO: Check if the guessed letter is in the secret or not and give the player feedback
        if is_guess_in_word(guess, secret_word):
            print("\nCorrect!")
        else:
            print("\nSorry, that letter is not in the word")
            guesses_left -= 1

        # Output everything to user each time
        print(f"\nYour guesses: {','.join(letters_guessed)}\n")
        print(f"{guesses_left} guesses left\n")
        print(get_guessed_word(secret_word, letters_guessed) + '\n')

    print("\nSorry, you lost!")
    return play_again()


def test():
    pass
    #print(is_guess_in_word('s', secret_word))
    #print(get_guessed_word(secret_word, letters_guessed))

#These function calls that will start the game

#test()
running = True
while running:

    start_game()
    word_with_guesses = []
    letters_guessed = []
    guesses_left = 7
    secret_word = load_word()
    running = spaceman(secret_word, word_with_guesses, letters_guessed, guesses_left)
