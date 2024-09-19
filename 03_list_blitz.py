"""
Task 1: Create a list
Create a list with 4 elements and print it.
"""
elements = ["fire","water","earth","air"]
print(elements)
"""
Task 2: Add Element to a List
Add an element to the end of the list. Print the updated 
list.
"""
elements.append("lighting")
print(elements)

"""
Task 3: Remove Element from a List
Remove a specific element from the list. Print the 
updated list.
"""
del elements[2]
print(elements)
"""
Task 4: Modify Element in a List
Modify an element at a specific index with a new value. 
Print the updated list.
"""
elements[1] = "ang"
print(elements)

"""
Task 5: Append Multiple Elements to a List
Append multiple elements to the end of the list. Print 
the updated list.
"""
black = ["avatar","toph"]
elements.append(black)
print(elements)
"""
Task 6: Delete Element at a Specific Index
Delete an element at a specific index. Print the updated 
list.
"""
del elements[0]
print(elements)
"""
Task 7: Subsetting lists
Create a new variable equal to the first 2 items of your list
Then print out the new variable
"""
baki = elements[1:3] 
print(elements)
"""
Task 8: Extend a List
Extend the list with the elements of another list. Print 
the updated list.
"""
elements_a = ["fire","ang"]
elements_b = ["lighting","avatar"]

elements = elements_a + elements_b
print(elements)