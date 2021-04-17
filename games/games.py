import fork
import guess


def choose_game():
    print_choose_game_message()

    game = int(input("\nWhich game? "))

    if game == 1:
        print("\nPlaying fork")
        fork.play()
    elif game == 2:
        print("\nPlaying guess")
        guess.play()


def print_choose_game_message():
    print("\n*********************************")
    print("*******Choose the game!*******")
    print("*********************************")
    print("\n(1) Fork (2) Guess")


if __name__ == "__main__":
    choose_game()
