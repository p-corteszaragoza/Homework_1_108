# description
""""
    Script: Simple Calculator
    Author: Paola Cortes
    Year: 2021
    Functionality: Basic Mathemathical operations
"""

# imports
# globals

# functions


def print_menu():
    print("-" * 30)
    print(" PyCalc")
    print("-" * 30)
    print("[1] - Sum")
    print("[2] - Subtract")
    print("[3] - Multiplication")
    print("[4] - Division")
    print("[5] - Is it odd ?")
    print("[q] - Quit")


# instructions
selected_option = ""
while(selected_option != "q"):
    print_menu()
    selected_option = input("Please select an option: ")
    print(selected_option)

    if(selected_option == "q"):
        break

    number_1 = int(input("Input number 1: "))
    if(selected_option != "5"):
        number_2 = int(input("Input number 2: "))

    if(selected_option == "1"):
        res = number_1 + number_2
    elif(selected_option == "2"):
        res = number_1 - number_2
    elif(selected_option == "3"):
        res = number_1 * number_2
    elif(selected_option == "4"):
        if(number_2 == 0):
            print("Error")
            res = 0
        else:
            res = number_1 / number_2
    elif(selected_option == "5"):
        res = number_1 % 2
        if(res):
            print("Odd Number")
        else:
            print("Even Number")

    print(res)

print("Good bye!")
