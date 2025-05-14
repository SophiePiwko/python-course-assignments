import random

random_number = random.randint(1, 20)
debug = False

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