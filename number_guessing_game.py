import random

number_to_guess = random.randint(1, 100)
while True:
    try:
        choice = int(input("Guess the number between 1 and 100: "))

        if choice < number_to_guess:
            print("Too low!")
        elif choice > number_to_guess:
            print("Too high!")
        else:
            print("Congratulations! You guessed the number")
    except ValueError:
        print("Please enter a valid number")
