import random

random_number = random.randint(1, 20)
debug = False
move_mode = False

while True:
    
    if debug:
        print(f"[Debug] The random number is: {random_number}")
    
    guess = input("Pick a number between 1 and 20, x to exit the game, s to show the number of d for the debug toggle. What is your pick?").strip()

    if guess.lower() == 'x':
        print("Game exited.")
        break

    elif guess.lower() == 's':
        print(f"The secret number is: {random_number}")

    elif guess.lower() == 'd':
        debug = not debug
        print(f"Debug mode {'on' if debug else 'off'}")

    elif guess.lower() == 'm':
        move_mode = not move_mode
        print(f"Move mode {'on' if move_mode else 'off'}")
        continue

    elif guess.isdigit():

        if random_number < int(guess):
            print("Your number is larger than the random number")

        elif random_number > int(guess):
            print("Your number is smaller than the random number")
        
        else:
            print("You guessed correct!")
            break

    else:
        print(" Invalid input. Please enter a number or x to exit the game")

    if move_mode:
        random_number += random.choice([-2, -1, 0, 1, 2])
        random_number = max(1, min(20, random_number))