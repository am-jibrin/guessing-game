import random

def guess_the_number():
    numbertoguess = random.randint(1, 100)  # Generates a number between 1 and 100
    attempts =3
    
    print("Welcome to the Number Guessing Game! Try to guess the number between 1 and 100.")

    while True:
        userguess = int(input("Enter your guess: "))  # Get user's guess
        attempts -= 1
        
        if userguess < numbertoguess:
            if numbertoguess - userguess > 10:
                print("Way too low, Try something higher.")
            else:
                print("A bit too low, You're close!")
        elif userguess > numbertoguess:
            if userguess - numbertoguess > 10:
                print("Way too high, Try something lower.")
            else:
                print("A bit too high,  Almost there!")
        else:
            print(f"Congrats! You guessed the number {numbertoguess} in {attempts} attempts.")
            break

# Start the game
guess_the_number()















 