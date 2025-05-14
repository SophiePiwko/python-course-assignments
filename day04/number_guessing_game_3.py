import random

random_number = random.randint(1, 20)

while True:
    guess = input("Pick a number between 1 and 20. What's your number?").strip()
    
    if guess.lower() == 'x':
        print("Game exited.")
        break

    if guess.lower() == 's':
        print(f"The secret number is: {random_number}")

    if guess.isdigit():

        if random_number < int(guess):
            print("Your number is larger than the random number")

        elif random_number > int(guess):
            print("Your number is smaller than the random number")
        
        else:
            print("You guessed correct!")
            break

    else:
        print(" Invalid input. Please enter a number or x to exit the game")