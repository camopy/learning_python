import random


def play():
    print_start_game_message()

    difficulty = choose_difficulty()
    life = setLife(difficulty)

    secret_number = random.randrange(1, 101)
    points = 1000

    for round in range(1, life + 1):
        print("\nYou are at your {} try from {}".format(round, life))

        guess_str = input("\nType a number from 1 to 100: ")
        print("You typed: ", guess_str)
        guess = int(guess_str)

        if guess < 1 or guess > 100:
            print("You typed a number outside the allowed range")
            continue

        won = guess == secret_number
        greater = guess > secret_number
        lower = guess < secret_number

        if won:
            print("\nYou found it!")
            break
        else:
            if greater:
                print("Wrong! Your guess was higher than the secret number.")
            elif lower:
                print("Wrong! Your guess was lower than the secret number.")
            lost_points = calculate_lost_points(secret_number, guess)
            points = points - lost_points

    if guess != secret_number:
        print("\nYou lost")
        print("The secret number was: ", secret_number)

    print("Points: ", points)
    print("\nGame over")


def choose_difficulty():
    print("\nWhat difficulty do you want?")
    print("(1) Easy (2) Normal (3) Hard")

    return int(input("\nChoose difficulty: "))


def calculate_lost_points(secret_number, guess):
    return round(abs(secret_number - guess) / 3)


def setLife(difficulty):
    if difficulty == 1:
        return 20
    elif difficulty == 2:
        return 10
    else:
        return 5


def print_start_game_message():
    print("\n*********************************")
    print("Welcome to the Guess game!")
    print("*********************************")


if __name__ == "__main__":
    play()