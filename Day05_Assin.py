'''1. Write a Python program that takes two numbers as input from the user and
performs the following operations:
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Modulus
6. Exponentiation
7. Floor division'''

# define a function for addition
def addition (num1,num2):
    print(f"{num1} + {num2} ={num1+num2}")

# define a function for subtraction
def subtraction (num1,num2):
    print(f"{num1} - {num2} ={num1-num2}")    

# define a function for multiplication
def multiplication (num1,num2):
    print(f"{num1} * {num2} ={num1*num2}")

# define a function for division
def division (num1,num2):
    print(f"{num1} / {num2} ={num1/num2}")

# define a functionn for modulus
def modulus (num1,num2):
    print(f"{num1} % {num2} ={num1 % num2}")
    
# define a function for exponentiation
def exponentiation (num1,num2):
    print(f"{num1} ** {num2} ={num1**num2}")

# define a function for floor division
def floor_division (num1,num2):
    print (f"{num1} // {num2} ={num1//num2}")


# using while loop for repeting this oprations according the wish of the user
while True:
    user_opinion = input("Enter (Y) if you want to continue......\nEnter (N) if you want to leave!").upper()
    
    if user_opinion == "Y":
        # get the input from user 
        num1=float(input("Enter Your first number:"))
        num2=float(input("Enter Your second number:"))
        operator=input("Select the operator (+, -, x, /, %, **, //) :")
        
        # Call the function of addition if user input "+"
        if operator == "+":
            addition (num1,num2)
        
        # Call the function of subtraction if user input "-"
        elif operator == "-":
            subtraction (num1,num2)
            
        # Call the function of multiplication if user input "x"
        elif operator == "x":
            multiplication(num1,num2)
        
        # Call the function of division if user input "/"
        elif operator == "/":
            division (num1,num2)
            
        # Call the function of modulus if user input "%"
        elif operator == "%":
            modulus (num1,num2)
            
        # Call the function of exponentiation if user input "**"
        elif operator == "**":
            exponentiation (num1,num2)
            
        # Call the function of exponentiation if user input "//"
        elif operator == "//":
            floor_division (num1,num2)
        #Otherwise
        else:
            print ("Enter valid Operator")
    # Break the function if user want to exit
    else:
        break
'''
# 1. Declare a variable x = 10 and perform the following operations using assignment
# operators:'''

#( 1. Add 5 to x
x = 10
x += 5
print (x)

# 2. Subtract 3 from x
x = 10
x -= 3
print (x)

# 3. Multiply x by 2
x = 10
x *= 2
print (x)

# 4. Divide x by 4
x = 10
x /= 2
print (x)

# 5. Apply floor division with 2
x = 10
x //= 2
print (x)

# 6. Raise x to the power of 3)
x = 10
x //= 2
print (x)

'''# Section 2: Comparison &amp; Logical Operators'''

# 1. Write a Python program that takes two numbers as input and prints:
num1 = int ( input("Enter  First Number:"))
num2 = int ( input("Enter Second Number:"))

# 1. Whether the first number is equal to the second.
if num1==num2:
    print ("The first number is equal to the second.")
else:
    print ("The first number is Not equal to the second.")
    
# 2. Whether the first number is greater than the second.
if num1>num2:
    print ("The first number is greater than the second.")
else:
    print ("The first number is Not greater than the second.")
    
# 3. Whether the first number is less than or equal to the second.
if num1<=num2:
    print ("The first number is less than or equal to the second.")
else:
    print ("The first number is Not less than or equal to the second")
    

'''# 1. Given a = 5, b = 10, c = 15, write expressions that evaluate the following:'''
a = 5
b = 10
c = 15

# 1. Whether a is less than b AND b is less than c.
result1 = (a < b) and (b < c)
print("a < b AND b < c:", result1)

# 2. Whether a is greater than b OR b is greater than c.
result2 = (a > b) or (b > c)
print("a > b OR b > c:", result2) 

# 3. The negation of b being greater than a.
result3 = not (b > a)
print("NOT (b > a):", result3) 

'''# 1. Declare two lists:
# 2. Check and print whether:'''
# 1. Declare two lists:
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

# 1. list1 and list2 are the same object.
result1 = list1 == list2
print ("list1 and list2 are the same object:", result1)

# 2. list1 and list3 are the same object.
result2 = list3==list1
print("list1 and list3 are the same object:", result2)

# 1. Given_fruits = ["apple","banana","cherry"] check and print:

fruits = ["apple","banana","cherry"]

# 1. If "apple" is in fruits.
result1 = "apple" in fruits
print ("Apple is in Your List:",result1)

# 2. If "grape" is not in fruits.
result2 = "grape" not in fruits
print ("grape is not in Your List:",result2)



