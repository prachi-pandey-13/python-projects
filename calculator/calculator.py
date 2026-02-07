# Calculator Project

import math

print("=====Welcome to the Advanced Python Calculator=====")



def show_menu():
    print("\nWhat do you want to calculate?")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. Square Root")
    print("8. Exit")


while True:
    try:
        num1 = float(input("\nEnter number 1 : "))
        num2 = float(input("Enter number 2 : "))
        # Ask the user what to calculate
        show_menu()

        # Take the user choice
        choice = int(input("Enter your choice:- "))
        match choice :
            case 1:
                # Perform Addition
                Result = num1 + num2
                print("Addition of numbers is : ", round(Result, 2))
            case 2:
                # Perform Subtraction
                Result = num1 - num2
                print("Subtraction of numbers is : ", round(Result, 2))
            case 3:
                # Perform Multiplication
                Result = num1 * num2
                print("Product of numbers is : ", round(Result, 2))
            case 4:
                # Perform Division
                if num2 == 0:
                    print("Error: Division by zero is not allowed")
                else:
                    Result = num1 / num2
                    print("Division of numbers is : ", round(Result, 2))
            case 5:
                # Perform modulus
                if num2 == 0:
                    print("Error: Modulus by zero is not allowed")
                else:
                    Result = num1 % num2
                    print("Modulus of numbers is : ", round(Result, 2))
            case 6:
                # Perform power of number
                Result = num1 ** num2
                print("Power of number 1 is : ", round(Result,2))
            case 7:
                # Perform square root of a number
                print("1. Square root of number 1")
                print("2. square root of number 2")
                sqrt = int(input("Choose number:"))
                if sqrt == 1:
                    Result = math.sqrt(num1)
                    print("Square root of number 1 is : ", round(Result, 2))
                elif sqrt == 2:
                    Result = math.sqrt(num2)
                    print("Square root of number 2 is : ", round(Result, 2))
                else:
                    print("Please enter a valid number.")
            
            case 8:
                print("\nThankyou for using the calculator.")
                break 

            case _ :
                print("Invalid choice ! Try again.")
    

# If user enters an invalid value       
    except ValueError:
        print("Please enter a valid number.")