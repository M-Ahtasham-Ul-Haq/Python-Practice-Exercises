# # 1.Convert 5.7 to an integer and print the result.
num=5.7
num1=int(num) # Converting into an integer
print (num1)

# 2.Convert 10 to a floating-point number and print the result.
num=10
num1=float(num) # Converting into floating-point number
print (num1)

# 3.Convert 100 to a string and concatenate it with " is a number", then print the result.

num=100
string=str(num) # Converting "100" into String
print(string + " is a number")

# 1.Given the string text = "Python Programming", print: 
# 1.The first character

text = "Python Programming"
print (text[0]) # In Word "Python" the index of "P" is 0 and -18
print (text[-18])

# 1.Given the string text = "Python Programming", print:
# 2.The last character

text = "Python Programming"
print (text[17])
print (text[-1]) # In Word "Python" the index of "g" is 17 and -1

# 1.Given the string text = "Python Programming", print:
# 3.The substring "Programming" using slicing

text = "Python Programming"
substring=text[7:] # Extract the substring "Programming" using slicing 
print(substring)

# 1.Given the string text = "Python Programming", print:
# 4.The substring "thon" using negative indexing

text="Python Programming"
print(text[-16:-12]) # Extract the substring "Programming" using slicing 
print(substring)

# 1.Write a program that prints each character of "HELLO" in a new line using a for loop.
text="HELLO"
for char in text: # Loop through each character in the string 
    print (char)  # Print each character on a new line
    
# 1.Given sentence = " Python is FUN! ", apply the following methods and print the results: 
# 1.Convert the string to lowercase.

sentence = "Python is FUN!"
print(sentence.lower()) # Convert the string to lowercase using the lower() Built-in Function

# Given sentence = " Python is FUN! ", apply the following methods and print the results: 
# 2.Convert the string to uppercase.

sentence = "Python is FUN!"
print(sentence.upper()) # Convert the string to uppercase using the upper() Built-in Function

# Given sentence = " Python is FUN! ", apply the following methods and print the results: 
# 3.	Remove extra spaces from both ends.

sentence = "  Python is FUN! "
print(sentence.strip()) # Remove the left and right space from string using the strip() Built-in Function

# Given sentence = " Python is FUN! ", apply the following methods and print the results: 
# 4.	Replace "FUN" with "Awesome".

sentence = "Python is FUN!"
print(sentence.replace("FUN","Awesome")) # Replace one word with another using the replace() Built-in Function

# 1.	Given quote = "Learning Python is interesting", check if "Python" is in the string and print True or False.

quote = "Learning Python is interesting"
print("Python"  in quote) # Print True If word "Python" is in string

# 1. Print the following using escape sequences in a single print statement: 
# "Python's flexibility makes it powerful!"
# Learn\tCode\tInnovate

print ("\"Python's flexibility makes it powerful!\"\nLearn\tCode\tInnovates\b.")

# 1.	Given text = "Hello, World!", use the appropriate methods to: 
# 1.	Find the length of the string.

text = "Hello, World!"
print(len(text)) # Find the length of the string 

# Given text = "Hello, World!", use the appropriate methods to:
# 2.Check if the string starts with "Hello".

text = "Hello, World!"
print(text.startswith("Hello")) # Print True if string start with word "Hello"

# Given text = "Hello, World!", use the appropriate methods to:
# 3.	Split the string at ",".

text = "Hello,World!"
print(text.split(",")) # Split the string into two substrings from the specific place

# Given text = "Hello, World!", use the appropriate methods to:
# 4.	Count the occurrences of the letter "o".

text = "Hello,World!"
print(text.count("o")) 
 
# 1.	Concatenate "Python" and "Programming" with a space in between and print the result.
text_1="Python" 
text_2="Programming"
print(text_1+" "+text_2) 

# 1.	Write a program that takes a user’s name and age as input, then prints:
# "Hello, my name is [name] and I am [age] years old." using an f-string.

name=input("Enter Your Name:")
age=input("Enter Your Age:")
print(f"Hello, my name is {name} and I am {age} years old.")