import random
random_number = random.randint(1, 20)

while True:
    guess = input("Pick a number between 1 and 20. What's your number? ")

    if random_number < int(guess):
        print("Your number is larger than the random number")

    elif random_number > int(guess):
        print("Your number is smaller than the random number")
    
    else:
        print("You guessed correct!")
        break