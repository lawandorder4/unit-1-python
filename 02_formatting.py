"""
TASK 1:
Write code that checks if a user entered the correct password.
The password should not be case sensitive

"""
#i created a password then i wrote the input for the correct password then i created and If and else to correct the user of any mistake 
correct_passwrod = "Tuesday123"
password = input("type passwrod: ")

if correct_passwrod ==password:
    print("correct password")

else:
    print("incorrrect passord")

"""
TASK 2:
Write code that checks if a user inputs an empty string
If the string is empty, print "invalid" otherwise print "valid"
"""
string  = input("Enter a string:")

if string == "":
    print("invalid")

else: 
    print("valid")

"""
TASK 3:

Write a program that will replace the word "cat" with the word "dog"
It should replace all occurances regardless of captilization 
"""
import re

def replace_cat_with_dog(text):

    return text.replace("cat", "dog").replace("CAT","DOG").lower()

input_text = "The cat sat on the mat . I saw a cat and a Cat"
output_text = replace_cat_with_dog(input_text)

print(output_text)


"""
TASK 4:

Write a program that takes a person's name and age as input and prints it
"""
name = "santi"
age = 17
print(f"My name is {name} and I am {age} years old.")


"""
TASK 5:

Write a program that takes in two floats, and prints the quotient
The result should be rounded to the nearest tenth (1 decimal place)
"""

