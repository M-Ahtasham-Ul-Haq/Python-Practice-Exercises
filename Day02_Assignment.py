# 1. Write a Python script that prints &quot;Welcome to Python
#  Programming!&quot; to the console.

print("Welcome to Python")

# 2. Declare three variables: name, age, and city. Assign them
# appropriate values and print them in a single sentence.

name = "Ahtasham Ul Haq"
age = 21
city = "Faisalabad"
print(f"My name is {name} I am {age} years old, and I live in{city}.")

# 3. Swap the values of two variables without using a third variable.

a=5
b=10
print ("Befo(re swaping a =",a,",b =",b)
print ("After Swaping a =",b,",b =",a)


# Write a Python program that takes user input for their first name
# and last name and prints them in reverse order with a space in
# between.

user_first_name = input ("Enter Your First Name:")
user_last_name = input ("Enter Your last Name:")
print (user_last_name, user_first_name)

# # 5. Declare a variable to store a floating-point number. Convert it
# # into an integer and print both values.

num1 = 4.889
print (int(num1))
print (float(num1))

# Section 2: Data Types and Basic Operations
# 1. Identify the data type of the following variables and print the
# result:

a = 10
print(type(a))
b = 3.14
print(type(b))
c = "Python"
print(type(c))
d = True
print(type(d))

# 2. Perform and print the result of the following arithmetic
# operations:
# I. Addition of two numbers.
# II. Subtraction of two numbers
# III. Multiplication of two numbers
# IV. Division of two numbers
# V. Modulus operation

num1=15
num2=5
Addition = num1+num2
Subtraction = num1-num2
Multiplication = num1*num2
Division = num1/num2
Modulus = num1%num2
print (Addition)
print (Subtraction)
print (Multiplication)
print (Division)
print (Modulus)

# 3. Write a script that asks the user for their birth year and calculates
# their current age.

user_age = int(input ("Enter Your Birth Year:"))
current_year = 2025
your_age = current_year-user_age
print("Your age is :", your_age)

# 4. Create a script that converts temperature from Celsius to
# Fahrenheit.

user_temperature =int(input("Enter Temperature in Celsius : "))
temperature_in_Fahrenheit = (user_temperature*9/5) + 32
print ("Temperature in Fahrenheit :", temperature_in_Fahrenheit)

# 5. Write a Python program that takes two numbers as input and
# performs all basic arithmetic operations on them (addition,
# subtraction, multiplication, division) and prints the results.

num1=int(input("Enter Your First Number: "))
num2=int(input("Enter Your Second Number: "))
Addition = num1+num2
Subtraction = num1-num2
Multiplication = num1*num2
Division = num1/num2
print ("Addition:",Addition)
print ("Subtraction:",Subtraction)
print ("Multiplication:",Multiplication)
print ("Division:",Division)

# 6. Write a program to check if a given number is even or odd.
num1=int(input("Enter Your Number:"))
if num1 % 2 == 0:
    print(num1,"is an even number")
else:
    print(num1,"is an odd number")
    