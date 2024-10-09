"""
Exercise 1:
Write a Python program that prints the current date and time using the datetime module.
"""
from datetime import datetime 
my_dt = datetime.now() 
print(my_dt)

"""
Exercise 2:
Write a Python program that prints the current date and time using the datetime module.
Using the strftime function format the date in standard U.S. date format (MM/DD/YYYY)
"""
from datetime import date 
my_date = date.today()
my_string = my_date.strftime("%m/%d/%Y")
print(my_string)
"""
Exercise 3:
Using the strptime function, convert two strings into dates.
Then find the difference in days between the two.
"""
from datetime import datetime

# i am defining the data strings right here 
date_string1 = "2023-10-01"
date_string2 = "2024-10-01"

#right here im coveriting date srtrings 

date1 = datetime.strptime(date_string1, "%Y-%m-%d")
date2 = datetime.strptime(date_string2, "%Y-%m-%d")

difference = (date2 - date1).days

print(difference)
"""
Excercise 4:
Write a program that asks the user for their birthdate and calculates their current 
age using the datetime module.
"""

from datetime import datetime 

birthdate_str = input("Enter your birthday (Y/M/D): ")

birthday = datetime.strptime(birthdate_str, "%Y-%m-%d")


today = datetime.now()

age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

print(f"you are {age} years old.")



 