import pytest
from spaceman import is_word_guessed, is_guess_in_word, get_guessed_word

def test_is_word_guessed():
    assert is_word_guessed('panda', ['a', 'b', 's', 'r', 'p']) == False
    assert is_word_guessed('arch', ['s', 'n', 'r', 'p', 'a', 'e', 'c', 'h']) == True

def test_is_guess_in_word():
    assert is_guess_in_word('a', 'bananas') == True
    assert is_guess_in_word('e', 'car') == False
    assert is_guess_in_word('1', 'feud') == False

def test_get_guessed_word():
    assert get_guessed_word('socks', ['j', 's', 't', 'r', 'o']) == "s o _ _ s"


if __name__ == "__main__":
    # Run the test function
    test_is_word_guessed()
