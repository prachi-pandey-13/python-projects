import random

# computer select a number
number = random.randint(1,100)
print("Computer choose a number between 1 and 100.")
print("Try to guess it!")

guess = -1
number_of_guesses = 0

while guess != number:
    try:
        # guess the number
        guess = int(input("Guess the number:- ")) 
        number_of_guesses += 1
        if guess == number:
            print("You guessed the correct number!")
            print(f"You guessed it in {number_of_guesses} attempts.")
            break
            # if guessed number is smaller
        elif guess < number:
            print("You guessed the smaller number.Try Bigger One...")
            
            # if guessed number is greater
        elif guess > number:
            print("You guessed the greater number.Try Smaller One...")
        else:
            print("Invalid number.")
    # if not an integer value
    except ValueError :
        print("Please enter a valid number.")