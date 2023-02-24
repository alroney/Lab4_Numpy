# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 17:27:42 2022

@author: Andrew
Description: The program allows a user to input a phone # and zip code
to have checked for format errors. Then the user inputs 2 matricies and 
can choose an operation to have performed on those 2 matricies.
"""
import re #Regular Expression
import numpy as np

def start_game():
    """

    Returns
    -------
    choice : STRING
        User input for option to play or not.

    """
    print("Welcome to the Python Matrix Application")
    while True:
        choice = input("Do you want to play the Matrix Game? (y for yes n for no): ")
        if choice.lower() == 'y' or choice.lower() == 'n':
            return choice

        print("Invalid Input! Please Try Again")

def phone():
    """


    Returns
    -------
    phone_number : STRING
        User input of phone number.

    """
    while True:
        phone_number = input("Enter your phone number (xxx-xxx-xxxx): ")
        if not re.match("\\d{3}-\\d{3}-\\d{4}", phone_number):
            print("The phone number is not in (xxx-xxx-xxxx) format. Please retry: ")

        else:
            break

    return phone_number


def zipcode():
    """

    Returns
    -------
    zip_code : STRING
        User input of zip code.

    """
    while True:
        zip_code = input("Enter your zip code+4 (xxxxx-xxxx): ")
        if not re.match("\\d{5}-\\d{4}", zip_code):
            print("The zip code is not in (xxxxx-xxxx) format. Please retry: ")

        else:
            break

    return zip_code



#=========MATRIX=========#
def create_matrix():
    """
    Get user in put in a format of #_#_# with _ = space
    3 times to create a 3 by 3 matrix array of integers.

    Returns
    -------
    matrix : ARRAY OF INTEGERS
        User defined 3 by 3 matrix stored into an array.

    """
    matrix = []

    for i in range(3): #3 rows
        row = input().split()#Read string input and split.
        row = list(map(int, row))#Convert split value to int.
        matrix.append(row)#Add row to matrix one.

    return matrix


def print_matrix(matrix, string):
    """
    Display the giving matrix and string.

    Parameters
    ----------
    matrix : ARRAY OF INTEGERS
        User defined 3 by 3 matrix stored into an array.
    string : STRING
        Used to make the statement appropriate to the situation at hand.

    Returns
    -------
    None.

    """
    print("Your", string,"matrix is:")
    for i, value in enumerate(matrix):
        for j in range(3):
            print(matrix[i][j], end=" ")
        print()

def matrix_transpose_mean(result):
    """
    Print the transposed matrix and the mean of the rows and columns

    Parameters
    ----------
    result : ARRAY OF INTEGERS
        Result of an equation with matrix 1 and matrix 2.

    Returns
    -------
    None.

    """
    transposed_result = np.transpose(result)
    print_matrix(transposed_result, "transpose of resulting")

    print("Row and column mean values of the result are:")
    print("Row:", np.mean(result, axis = 1))
    print("Column:", np.mean(result, axis = 0))

def matrix_addition(matrix_one, matrix_two):
    """
    Addition on the two user supplied matricies.

    Parameters
    ----------
    matrix_one : ARRAY OF INTEGERS
        First matrix defined by user.
    matrix_two : ARRAY OF INTEGERS
        Second matrix defined by user.

    Returns
    -------
    None.

    """
    print("You chose Addition. The results are:")
    matrix_one = np.array(matrix_one)
    matrix_two = np.array(matrix_two)

    result = matrix_one + matrix_two #Equation
    print_matrix(result, "resulting")

    matrix_transpose_mean(result)


def matrix_subtraction(matrix_one, matrix_two):
    """
    Subtraction on the two user supplied matricies.

    Parameters
    ----------
    matrix_one : ARRAY OF INTEGERS
        First matrix defined by user.
    matrix_two : ARRAY OF INTEGERS
        Second matrix defined by user.

    Returns
    -------
    None.

    """
    print("You chose Subtraction. The results are:")
    matrix_one = np.array(matrix_one)
    matrix_two = np.array(matrix_two)

    result = matrix_one - matrix_two #Equation
    print_matrix(result, "resulting")

    matrix_transpose_mean(result)


def matrix_multiplication(matrix_one, matrix_two):
    """
    Multiplication on the two user supplied matricies.

    Parameters
    ----------
    matrix_one : ARRAY OF INTEGERS
        First matrix defined by user.
    matrix_two : ARRAY OF INTEGERS
        Second matrix defined by user.

    Returns
    -------
    None.

    """
    print("You chose Multiplication. The results are:")
    matrix_one = np.matrix(matrix_one)#function matrix for matrix multiplying.
    matrix_two = np.matrix(matrix_two)

    result = matrix_one * matrix_two #Equation
    result = np.array(result)#Put back into array to be read.
    print_matrix(result, "resulting")

    matrix_transpose_mean(result)


def matrix_element_multiplication(matrix_one, matrix_two):
    """
    Element Multiplication on the two user supplied matricies.

    Parameters
    ----------
    matrix_one : ARRAY OF INTEGERS
        First matrix defined by user.
    matrix_two : ARRAY OF INTEGERS
        Second matrix defined by user.

    Returns
    -------
    None.

    """
    print("You chose Element by Element Multiplication. The results are:")
    matrix_one = np.array(matrix_one)
    matrix_two = np.array(matrix_two)

    result = matrix_one + matrix_two #Equation
    print_matrix(result, "resulting")

    matrix_transpose_mean(result)


def play_matrix():
    """
    Create 2 matricies and conduct a math equation on the 2
    at the choice of the user.

    Returns
    -------
    None.

    """
    matrix_one = []
    matrix_two = []

    print("Enter your first matrix: ")
    matrix_one = create_matrix()
    print_matrix(matrix_one, "first")

    print("Enter your second matrix: ")
    matrix_two = create_matrix()
    print_matrix(matrix_two, "second")

    print("Select a Matrix Operation from the list below:")
    print("a. Addition")
    print("b. Subtraction")
    print("c. Matrix Multiplication")
    print("d. Element by element multiplication")
    print("e. Exit Matrix Operations")

    choice = ""
    while choice.lower() != "e":
        choice = input("Choice: ")
        #ADDITION
        if choice.lower() == "a":
            matrix_addition(matrix_one, matrix_two)

        #SUBTRACTION
        elif choice.lower() == "b":
            matrix_subtraction(matrix_one, matrix_two)

        #MULTIPLICATION
        elif choice.lower() == "c":
            matrix_multiplication(matrix_one, matrix_two)

        #ELEMENT BY ELEMENT MULTIPLICATION
        elif choice.lower() == "d":
            matrix_element_multiplication(matrix_one, matrix_two)

        elif choice.lower() == "e":
            print("Now leaving matrix operations...")

        else:
            print("Invalid Input! Please try again.")

#=========END MATRIX=========#


def exit_message():
    """
    Appropriate exit for the user.

    Returns
    -------
    None.

    """
    input("Thanks for playing\nPress ENTER to exit.")

def main():
    """
    Put everything together and in place to run.

    Returns
    -------
    None.

    """
    playit = start_game()
    if playit.lower() == "y":
        phone()
        zipcode()
        play_matrix()
        exit_message()

    else:
        exit_message()


main()#Run
