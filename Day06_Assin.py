# 1. Basic List Operations

# a) Create a list with duplicate values and print it.
fruits=["apple","banana","orange","pineapple", "strawbarry", "apple"]
print ( fruits )

# b) Find and print the length of the list using a built-in function.
fruits=["apple","banana","orange","pineapple", "strawbarry", "apple"]
print (len (fruits))

# c) Check and print the data type of your list.
fruits=["apple","banana","orange","pineapple", "strawbarry", "apple"]
print (type (fruits))

# 2. Accessing and Modifying Lists  Create a list of five items and
vegetables = ["Carrot", "Potato", "Tomato", "Onion", "Garlic"]

# a) access the second and last item using indexing.
vegetables = ["Carrot", "Potato", "Tomato", "Onion", "Garlic"]
print(f"{vegetables[1]}, {vegetables[4]}")

# b) Use negative indexing to print the second last item in the list.
vegetables = ["Carrot", "Potato", "Tomato", "Onion", "Garlic"]
print(vegetables[-2])

# c) Change the third item in the list to "Updated_Value";
vegetables = ["Carrot", "Potato", "Tomato", "Onion", "Garlic"]
vegetables[2]= "Pumpkin"
print (vegetables)

# 3. List Methods and Removal
# a) Remove an item by value and print the updated list.
vegetables = ["Carrot", "Potato", "Tomato", "Onion", "Garlic"]
vegetables.remove("Carrot")
print (vegetables)

# b) Remove an item by index using .pop() and print the list.
vegetables = ["Carrot", "Potato", "Tomato", "Onion", "Garlic"]
vegetables.pop(1)
print (vegetables)

# c) Use the del keyword to delete the entire list and try printing it.
vegetables = ["arrot", "Potato", "Tomato", "Onion", "Garlic"]
del vegetables[:] 
print (vegetables)

# 4. Sorting and Copying
# a) Create a list of numbers and sort them in ascending order.
numbers = [1,3,2,4,9,6,7,8,5]
numbers.sort()
print (numbers)

# b) Sort the list in descending order.
numbers = [1,3,2,4,9,6,7,8,5]
numbers.sort(reverse=True)
print (numbers)

# c) Make a copy of the sorted list using .copy() and print both lists.
numbers = [1,3,2,4,9,6,7,8,5]
numbers2 = numbers.copy()
print (numbers2)

# 5. Joining and Extending Lists
# a) Join two lists using the + operator and print the result.
numbers = [1,3,2,4,9,6,7,8,5]
vegetables = ["Carrot", "Potato", "Tomato", "Onion", "Garlic"]
join_list = numbers + vegetables
print (join_list)

# b) Extend a list using .extend() and print the updated list.
numbers = [1,3,2,4,9,6,7,8,5]
vegetables = ["Carrot", "Potato", "Tomato", "Onion", "Garlic"]
numbers.extend(vegetables)
print (numbers)

# 6. List Methods Usage
# a) Create a list with repeated values and count the occurrences of a specific value
# using .count().
vegetables2=["Asparagus", "Corn", "Leek", "Chili", "Turnip", "Asparagus"]
print(vegetables2.count("Asparagus"))

# b) Clear a list using .clear() and print it.
vegetables2=["Asparagus", "Corn", "Leek", "Chili", "Turnip", "Asparagus"]
vegetables2.clear()
print(vegetables2)

# c) Create a new list using the list() function and print its type.
name1=["Ahmed", "Muhammad", "Ali", "Hassan", "Hussain"]
name2 = list(name1)
print (type(name2))

# Sure! Here are additional questions to make the assessment more comprehensive:
# 7. Advanced List Manipulations
# a) Insert a new item at the second position in a list using .insert().
names=["Ahmed", "Muhammad", "Ali", "Hassan", "Hussain"]
names.insert(1,"Muhammad")

# b) Replace the first three items in a list with a new set of values.
names=["Ahmed", "Muhammad", "Ali", "Hassan", "Hussain"]
names[0:3]="apple", "banana", "cherry"
print(names)

# c) Reverse a list using a built-in method and print it.
names=["Ahmed", "Muhammad", "Ali", "Hassan", "Hussain"]
names.reverse()
print (names)

# 8. Finding Duplicates in a List
# a) Write a Python program to check if a list contains duplicate values.
def has_duplicates(list):
    return len(list) != len(set(list)) 

list = ["Ahmed", "Muhammad", "Ali", "Hassan", "Hussain","Ahmed","Muhammad"]
print(has_duplicates(list))

# b) Remove duplicates from a list and print the unique values.
list = ["Ahmed", "Muhammad", "Ali", "Hassan", "Hussain","Ahmed","Muhammad"]
def remove_duplicates(list):
     return (set(list))
print (remove_duplicates(list))

# 9. List Slicing and Iteration
# a) Extract and print a sublist containing the 2nd to 4th items from a given list.
names = ["Ahmed", "Muhammad", "Ali", "Hassan", "Hussain"]
sublist = names[2:5]
print (sublist)

# b) Use a loop to iterate over a list and print each item on a new line.
names = ["Ahmed", "Muhammad", "Ali", "Hassan", "Hussain"]
for name in names:
    print (name)

# c) Use list comprehension to create a new list that contains only even numbers from a
# given list of numbers.
numbers = [1,3,2,4,9,6,7,8,5]
new_list = []
new_list = [num for num in numbers if num % 2 ==0]      
print (new_list)

# 10. List Comparisons and Identity Operators
# a) Given two lists list1 and list2, check if they have the same elements but different
# memory locations.
list_1 = [1,2,3,4,5,6,7,8]
list_2 = [1,2,3,4,5,6,7,8]
if list_1 == list_2:
    print ("list_1 = list_2")
else:
    print ("list_1 != list_2")
    
if list_1 is list_2:
    print ("Address of list_1 = Address of list_2")
else:
    print ("Address of list_1 != Address of list_2")
    
# b) Use the is and == operators to compare two lists and explain the difference in their
# output.
list_1 = [1,2,3,4,5,6,7,8]
list_2 = [1,2,3,4,5,6,7,8]
if list_1 == list_2:
    print ('\n"==" Compare the content or values in the lists_1 and list_2.\n')
else:
    print ("list_1 != list_2")
    
if list_1 is list_2:
    print ("Address of list_1 = Address of list_2")
else:
    print (' Where "is" Compare the Address of both lists. Every list has different address in memory location\n')
    
# a) Create a list that contains another list (nested list). Access and print an item from
# the nested list.
list = [[1, 2, 3], ["Muhammad", "Hassan", "Hussain"], ["Asparagus", "Corn", "Leek", "Turnip",]]
print (f"{list[0][1]},{list[1][1]},{list[2][3]}")

# b) Flatten a nested list into a single list using list comprehension.
list = [[1, 2, 3], ["Muhammad", "Hassan", "Hussain"], ["Asparagus", "Corn", "Leek", "Turnip",]]
flatten_list = []
#loop for sublists
for sublist in list:
    #loop for items in sublist
    for items in sublist:
        flatten_list.append(items)
print(flatten_list)

# 12. List Challenges
# a) Create a program that takes user input to build a list dynamically and removes
# duplicate values.
list1 = (input("Enter Your list: ")).split(" ")

def has_duplicates(list1):
    return len(list1) != len(set(list1)) 

print(has_duplicates(list1))

def remove_duplicates(list1):
     return (set(list1))
 
print (remove_duplicates(list1))

# a) Create a program that takes user input to build a list dynamically and removes
# duplicate values.
dynamic_list = []
unique_list=[]
while True:
    user_list = input("Enter your list item (type stop to exit):").title()
    if user_list != 'Stop':
        dynamic_list.append(user_list)
        for item in dynamic_list:
            if item not in  unique_list:
                unique_list.append(item)
    else:
        break
    
print(dynamic_list)
print(unique_list)

# b) Write a Python function that returns the most frequent item in a given list.
def most_frequent(list1,max_count):
    max_count = 0
    most_frequent_item = None
    
    for item in list1:
        count = list1.count(item)
        if count > max_count:
            max_count = count 
            
            most_frequent_item = item
            
    return most_frequent_item,max_count

max_count = 0
list1 = [1,2,3,1,2,2,2,2,3,3,3,3,3,3,3,3]
print(most_frequent(list1,max_count))
# c) Create a list with mixed data types (integers, strings, booleans) and filter out only
# the numeric values.
mix_list = [313,3.13,True,"String",6 + 7j, 53,23.23]

num_list = []
for item in mix_list:
    if type(item) in [int,float]:
        num_list.append(item)
        
print(f"The numeric values is {num_list}")