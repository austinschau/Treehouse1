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

    #introduction to the game
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

    while replay == 'y':

        randomNumber = random.randint(0,10)
        guessCount = 1

        while True:
            # variable for holding guess count as a string
            displayCount = ""

            # format displayCount
            if guessCount == 1:
                displayCount = "1st"
            elif guessCount == 2:
                displayCount = "2nd"
            elif guessCount == 3:
                displayCount = "3rd"
            else:
                displayCount = str(guessCount) + "th"

            # variable stores the users guess
            userGuess = ""
            #Verify user input
            while True:
                userGuess = input("Please enter your  " + displayCount + " guess: ")
                try:
                    userGuess = int(userGuess)
                except ValueError:
                    print("Sorry that is not a valid guess. Your guess must be an integer number.")
                    continue
                if 0<= userGuess <= 10:
                    break
                else:
                    print("That number is not in the pre discussed range...it must be 1-10")

            #check if users guess is correct
            if int(userGuess) == randomNumber:
                print("Wow! You guessed it on your " + displayCount + " try...")
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
                    randomNumber = random.randint(0, 10)
                    break

                elif replay.lower() == "n":
                    print("The cake is a lie!!!")
                    break
                else:
                    print("I don't know what that means..but bye!")
                    break

            elif int(userGuess) > randomNumber:
                print("Sorry, your guess was too high.")
            else:
                print("Sorry, your guess was too low.")

            guessCount += 1


# Kick off the program by calling the start_game function.
start_game()