import os
import time
import random

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


class Result(object):

    def __init__(self, dict_word, found):
        self.dict_word = dict_word
        self.found = found



def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s


def read_word():
    words = []
    with open("./python-intermedio/archivos/data.txt", "r", encoding="utf-8") as f:
        for line in f:
            words.append(line.strip())
    data = {
        "data_input": words,
        "len_input": len(words)
    }
    return data


def error_message():
    time.sleep(2.4)
    os.system('cls||clear')


def game_over():
    os.system('cls||clear')
    print(HANGMANPICS[len(HANGMANPICS) - 1])
    print("Suerte para la próxima!!!")
    time.sleep(2.4)
    os.system('cls||clear')


def print_word_to_find(word_to_find, dict_word):
    banner = ""
    for letter in word_to_find:
        if letter in dict_word:
            if dict_word[letter]:
                banner = banner + letter + " "
            else:
                banner = banner + "_ "
        else:
            banner = banner + "_ "
    print(banner)


def get_letter(attempts, word_to_find, dict_word):
    band = False
    letter = ""
    while not band:
        print(HANGMANPICS[attempts])
        print()
        print_word_to_find(word_to_find, dict_word)
        print()
        letter = input("Ingrese la letra: ")
        is_number = False
        try:
            int(letter)
            is_number = True
        except Exception:
            is_number = False

        if is_number:
            print("Solamente se aceptan letras")
            error_message()
        elif len(letter) != 1:
            print("Favor de ingresar una sola letra")
            error_message()
        else:
            band = True
    return letter.upper()


def match_word(word, letter, matches):
    found = False
    if letter in word:
        matches[letter] = True
        found = True
    return Result(matches, found)


def create_dict(word):
    dict_word = {}
    for letter in word:
        # if letter[1] in dict_word:
        #     dict_word[letter[1]] += 1
        # else:
        #     dict_word[letter[1]] = 1
        if not letter[1] in dict_word:
            dict_word[letter[1]] = False
    return dict_word


def winner_player(word):
    os.system('cls||clear')
    print(word)
    print("Felicidades, ganaste!!!")
    time.sleep(2.4)
    os.system('cls||clear')


def play_game():
    game_is_over = False
    attempts = 0
    data = read_word()
    index = random.randrange(0, data["len_input"] - 1)
    original_word = data["data_input"][index].upper()
    word = normalize(original_word)
    word_in_list = list(enumerate(word))
    dict_word = create_dict(word_in_list)

    while not game_is_over:
        winner = True
        os.system('cls||clear')
        letter = get_letter(attempts, word, dict_word)
        result = match_word(word, letter, dict_word)
        if not result.found:
            attempts += 1
        dict_word = result.dict_word
        for key, value in dict_word.items():
            if not value:
                winner = False
        if winner:
            winner_player(original_word)
            game_is_over = True
        elif attempts == len(HANGMANPICS) - 1:
            game_over()
            game_is_over = True


if __name__ == "__main__":
    play_game()
