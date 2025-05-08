# 1. Create a tuple
# Write a Python program to create a tuple containing the numbers 1 to 5 and print it.
tuple1 = (1,2,3,4,5)
print("Tuple :", tuple1)

# 2. Access tuple elements
# Write a Python program to access the third element of the tuple (10, 20, 30, 40, 50).

tuple1 = (10, 20, 30, 40, 50)
print ("Third Element in Tuple is", tuple1[2])

# 3. Tuple unpacking
person = ("Alice", 25, "Engineer")
name, age, profession = person
print (name,age,profession)

# 4. Concatenate two tuples
# Write a Python program to concatenate the following tuples and print the result:
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenate_tuple = tuple1 + tuple2
print ("Concatinated Tuple :",concatenate_tuple)

# 5. Check for an item in a tuple

tuple1 = (1, 3, 5, 7, 9)
print("Is 7 in Tuple:",7 in tuple1)

# 6. Tuple slicing
# Given the tuple (10, 20, 30, 40, 50, 60, 70), write a program to extract the middle three elements and print them.
tuple1=(10, 20, 30, 40, 50, 60, 70)
middle_three = tuple1 [2:5]
num1, num2, num3 = middle_three
print ("Middle Three Elements are", num1, num2, num3)

# 7. Count occurrences in a tuple
# Given the tuple (1, 2, 3, 2, 4, 2, 5, 2), write a Python program to count how many times 2 appears.
tuple1 = (1, 2, 3, 2, 4, 2, 5, 2)
count_of_2 = tuple1.count(2)
print(f"2 Appears in tuple {count_of_2} times")

# 8. Find the index of an element
# Write a program to find the index of 50 in the tuple (10, 20, 30, 40, 50, 60).
tuple1 = (10, 20, 30, 40, 50, 60)
index_of_50 = tuple1.index(50)
print("The index of 50 is",index_of_50)

# 9. Convert a list to a tuple
# Write a Python program to convert the list [10, 20, 30, 40, 50] into a tuple.
list1 = [10, 20, 30, 40, 50]
tuple1 = tuple(list1)
print(tuple1)

# 10. Reverse a tuple
# Given the tuple (1, 2, 3, 4, 5), write a program to reverse it.
tuple1 = (1, 2, 3, 4, 5)
reverse_tuple = tuple1[::-1]
print("Reversed Tuple :", reverse_tuple)