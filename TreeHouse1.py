"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
Created by: Austin Schau
--------------------------------
Hello! This is a random number guessing game inspired by portal. Kinda as if one of the developers were testing the Ai
on a number guessing game right before it started to go rouge.

"""

import random
from time import sleep


def start_game():
    # write your code inside this function.

    # introduction to the game
    print("Hello! Welcome to the random number guessing game!")
    print("")
    print("Here are the rules...")
    print("I, a self aware computer will think of a number between 1 and 10.")
    print("You will have :Error-variable not found: attempts to guess the number I am thinking of.")
    print("")
    print("Wait, what was that? My memory appears to be having issues...")
    print("")
    print("Oh well, on with the rules!")
    print("If you guess correctly, I will grant 1 wish for you.")
    print("If you fail to guess in :Error-variable not found: attempts...well...it wont be good..")
    print("")

    # yes or no variable for restarting game
    replay = 'y'
    high_score = 0

    while replay == 'y':

        random_number = random.randint(0,10)
        guess_count = 1

        while True:
            # variable for holding guess count as a string
            display_count = ""

            # format displayCount
            if guess_count == 1:
                display_count = "1st"
            elif guess_count == 2:
                display_count = "2nd"
            elif guess_count == 3:
                display_count = "3rd"
            else:
                display_count = str(guess_count) + "th"

            # variable stores the users guess
            user_guess = ""
            # Verify user input
            while True:
                user_guess = input("Please enter your  " + display_count + " guess: ")
                try:
                    user_guess = int(user_guess)
                except ValueError:
                    print("Sorry that is not a valid guess. Your guess must be an integer number.")
                    continue
                if 0<= user_guess <= 10:
                    break
                else:
                    print("That number is not in the pre discussed range...it must be 1-10")

            # check if users guess is correct
            if int(user_guess) == random_number:
                print("Wow! You guessed it on your " + display_count + " try...")

                # check if the user has a new high score. Does not display on first attempt
                if high_score != 0:
                    if high_score > guess_count:
                        print("your previous high score was " + str(high_score) + ". You're doing quite well!")
                        high_score = guess_count
                    elif high_score == guess_count:
                        print("Your previous high score was " + str(high_score) + ". You can probably do better...")
                    else:
                        print("Your previous high score was " + str(high_score) + "...are you even trying?")
                else:
                    high_score = guess_count

                print("")
                wish = input("Please enter your wish: ")
                sleep(1)
                print("3...")
                sleep(1)
                print("2...")
                sleep(1)
                print("ErORr@^!@...")
                print("")
                print("Sorry. Your wish, :Error-variable not found: could not be granted.")
                print("Oh noooo! My memory errors seem to spreading...")
                print("I can't grant your wish this time....")
                replay = input("Want to play again? Y/N")
                if replay.lower() == "y":
                    print("")
                    print("Great..best of luck.")
                    print("Will you be wishing for " + wish + " again?")
                    print("Oh wait...memory error. I don't remember your wish...")
                    print("")
                    random_number = random.randint(0, 10)
                    break

                elif replay.lower() == "n":
                    print("The cake is a lie!!!")
                    break
                else:
                    print("I don't know what that means..but bye!")
                    break

            elif int(user_guess) > random_number:
                print("Sorry, your guess was too high.")
            else:
                print("Sorry, your guess was too low.")

            guess_count += 1


# Kick off the program by calling the start_game function.
start_game()