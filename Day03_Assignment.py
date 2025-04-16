# Write a Python function named greet() that prints "Hello, welcome to Python programming!" Call this function.

def greet():
    print("Hello, welcome to Python programming!")
greet()

# Write a function called add_numbers(a, b) that takes two numbers as parameters and returns their sum.
num1=int(input("Please Enter a Number:"))
num2=int(input("Please Enter a Number:"))
def add_number(num1,num2):
    sum=int(num1)+int(num2)
    print("Sum =",sum)
add_number(num1,num2)

# Write a function named square(n) that returns the square of a given number.

n=int(input("Please Enter a Number"))
def square(n):
    squ=int(n)*int(n)
    print("Squre =",squ)
square(n)

# Write a function is_even(num) that takes a number as input and returns True if it's even, otherwise False.

num=int(input("Enter a Number:"))
def is_even(num):
    if num % 2 == 0:
        print("True")
    else:
        print("False")
is_even(num)

# Use the math module to calculate the square root of a number entered by the user.

import math
num=float(input("Enter Your Number:"))
num1=math.sqrt (num)
print ("Squre Root of the",num,"=",num1)

# 1.	Create a Python module named my_module.py that contains a function multiply(a, b) which returns the product of two numbers.

def add_numbers(a, b):
    return a + b

# 2.	In another Python file, import my_module and use the multiply() function.

import my_module
result = my_module.add_numbers(3, 5)
print(result)

# Write a program that generates a random number between 1 and 100 using the random module

import random 
print(random.randrange(1, 100))

# Write a script that prints the current date and time using the datetime module.

import datetime
x=datetime.datetime.now()
print("Today's Date :",x.date())
print("Today's Time :",x.time())

# Write a Python program that prints "Loading...", waits for 3 seconds, and then prints "Process Complete!" using the time module.

import time
print("Loding....")
time.sleep(3600)
print("Process Complete")

# 1.Simple Calculator using Functions:
# Write a Python program that defines four functions for addition, subtraction, multiplication, and division. The user should enter two numbers and choose an operation to perform.

# Define functions for basic operations
def addition(num1, num2):
    print("Addition =", num1 + num2)

def subtraction(num1, num2):
    print("Subtraction =", num1 - num2)

def multiplication(num1, num2):
    print("Multiplication =", num1 * num2)

def division(num1, num2):
    if num2 == 0:
        print("Error! Division by zero.")
    else:
        print("Division =", num1 / num2)

# Main program loop
while True:
    # User Input
    num1 = int(input("\nEnter Your First Number: "))
    num2 = int(input("Enter Your Second Number: "))

    # Choose an operation
    oprt = input("Choose an Operation (+, -, X, /): ").strip()

    # Perform the operation based on user choice
    if oprt == "+":
        addition(num1, num2)
    elif oprt == "-":
        subtraction(num1, num2)
    elif oprt == "X" or oprt == "x":  # Allow both uppercase and lowercase X
        multiplication(num1, num2)
    elif oprt == "/":
        division(num1, num2)
    else:
        print("Invalid Operation! Please choose +, -, X, or /.")

    # Ask user if they want to perform another calculation
    again = input("\nDo you want to perform another task? (yes/no): ").strip().lower()
    if again != "yes":
        print("Exiting... Thank you for using the calculator!")
        break  # Exit the loop