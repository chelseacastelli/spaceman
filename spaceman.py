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
    '''
    A function that clears the terminal for better readability
    '''
    _ = call('clear' if os.name =='posix' else 'cls')

def start_game():
    '''
    A function that outputs the starting menu for the game
    '''
    print("\nWelcome! Let's play Spaceman :)\nTry guessing the secret word one letter at a time\nbefore the Spaceman is drawn.\n")

def play_again():
    '''
    A function that asks the user if they want to play again

    Returns:
        bool: True if they say yes, False otherwise
    '''
    play_again = user_input("Would you like to play again? (y/n): ")
    if play_again.lower() == 'y':
        clear()
        return True
    clear()
    return False

def valid_input(guess):
    '''
    A function that checks the user input is valid. Checks for more than one character, if the letter was already guessed, or if a number is inputted.

    Returns:
        bool: True if the input was valid, False otherwise
    '''

    if len(guess) > 1:
        print("Guess only one letter. ")

    elif guess in letters_guessed:
        print("You already guessed that letter. ")

    elif guess.isnumeric():
        print("No numbers. ")
    else:
        return True

    return False

def is_word_solved():
    '''
    A function that checks if the word has been guessed by searching for any more blanks

    Returns:
        bool: True if word has been guessed (no more blanks), False otherwise
    '''
    if '_' not in get_guessed_word(secret_word, letters_guessed):
        return True
    return False

def spaceman(secret_word, word_with_guesses, letters_guessed, guesses_left):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''

    #TODO: show the player information about the game according to the project spec
    print(f"There are {len(secret_word)} letters in this word so you get {len(secret_word)} guesses. Choose wisely.\nGo!\n\n{get_guessed_word(secret_word, letters_guessed)}")
    guesses_left = len(secret_word)

    while guesses_left > 0:

        #TODO: Ask the player to guess one letter per round and check that it is only one letter
        guess = user_input("\nEnter your guess: ")
        while not valid_input(guess):
            guess = user_input("Try again: ")

        letters_guessed.append(guess)

        # Clear terminal for cleaner output
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

        # Check if every letter has been guessed (no more blanks)
        if is_word_solved():
            clear()
            print('\n')
            print(get_guessed_word(secret_word, letters_guessed))
            print('\n')
            print(f"You got it! & with {guesses_left} guesses left.. great job!\n")
            return play_again()

        elif not is_word_solved() and guesses_left == 0:
            print(f"\nSorry, you lost! The word was {secret_word}\n")
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
    guesses_left = 0
    secret_word = load_word()
    running = spaceman(secret_word, word_with_guesses, letters_guessed, guesses_left)
