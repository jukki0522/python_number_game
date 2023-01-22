import random

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
               19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

number = random.choice(number_list)

def check_user_input(guess_number):
   try:
       guess_number = int(guess_number)
   except ValueError:
       print("That's not a number...")
       exit()

def number_game():
    global guesses
    global guess_number
    guesses = 5
    guess_number = input("guess the number!(You have %i guesses remaining)" % guesses)
    check_user_input(guess_number)
    if guess_number == number:
        print("Congratulations! You've guessed the number correctly!")
    else:
        if guess_number - number > 5 or number - guess_number > 5:
            print("Too cold! Try again")
        if 5 >= guess_number - number >= -5:
            print("You're close! Try again!")
        else:
            print("Too cold! Try again!")
        guesses = guesses - 1
        number_game_1()

def number_game_1():
    global guesses  # get the guesses (global variable)
    guess_number = input("guess the number!(You have %i guesses remaining)" % guesses)
    check_user_input(guess_number)
    guess_number = int(guess_number)
    if guess_number == number:
        print("Congratulations! You've guessed the number correctly!")
        exit()
    else:
        guesses = guesses - 1
        if guesses == 0:
                print("Unfortunately, you've gotten your number wrong for 5 times in a row. Better luck next time!")
                print("By the way, the number was %i" % number)
                exit()
        if guess_number - number > 5 or number - guess_number > 5:
            print("Too cold! Try again")
        if 5 > guess_number - number > 0:
            print("You're close! Try again!")
        else:
            print("Too cold! Try again!")
        while guesses > 0:
            number_game_1()


y_n_prob = input("Would you like to play the number guessing game?")
y_n_prob = str.lower(y_n_prob)
if "yes" in y_n_prob:
    print("You have 5 guesses. Good luck!")
    number_game()
else:
    print("Goodbye!")
