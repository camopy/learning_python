import random
import os


def play():
    print_opening_message()

    secret_word = get_secret_word()
    guessed_letters = init_guessed_letters(secret_word)

    forked = False
    found = False

    errors = 0
    life = 7

    while not found and not forked:
        print("\nYou have {} tries".format(life - errors))
        print("Guess the word: ", guessed_letters)
        guess = input("What letter? ").strip().upper()

        if guess in guessed_letters:
            print("You already found this letter, try another one")
        elif guess in secret_word and guess not in guessed_letters:
            fill_guessed_letters(secret_word, guessed_letters, guess)
        else:
            print("Letter not found")
            errors += 1
            print_fork(errors)

        found = "_" not in guessed_letters
        forked = errors == life

    if found:
        print_winner_message()
    else:
        print_looser_message(secret_word)


def print_opening_message():
    print("\n*********************************")
    print("***Welcome to Fork game!***")
    print("*********************************")


def get_secret_word():
    words = []
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, "words.txt")
    with open(filename, "r") as wordsFile:
        for line in wordsFile:
            words.append(line.strip())

    return words[random.randrange(0, len(words))].upper()


def fill_guessed_letters(secret_word, guessed_letters, guess):
    index = 0
    for letter in secret_word:
        if letter == guess:
            print("Found the letter {} at {} position".format(letter, index))
            guessed_letters[index] = letter
        index += 1


def init_guessed_letters(secret_word):
    return ["_" for letter in secret_word]


def print_looser_message(secret_word):
    print("\nYou were forked!")
    print("The correct word was {}".format(secret_word))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def print_winner_message():
    print("\nCongratulations, you found the secret word!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def print_fork(errors):
    print("  _______     ")
    print(" |/      |    ")

    if errors == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if errors == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if errors == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if errors == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if errors == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if errors == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if errors == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if __name__ == "__main__":
    play()
