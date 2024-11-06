"""
Task 1: Greeting
Write a function that takes a name as a 
parameter and prints a greeting message like "Hello, [name]!".
"""
# started by creating my funtion 
def greet(name):
    print(f"hello , {name}!")

greet("alice")

"""
Task 2: Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""
def square(number):
    return number ** 2

result = square(5)
print(result)

"""
Task 3: Even or Odd
Write a function that takes a number as a argument that 
returns `True` if the number is even, and `False` otherwise.
""" 
def is_even(number):
    return number % 2 == 0

result = is_even(4)
print(result)


result = is_even(5)
print(result)

"""
Task 4: Area of a Rectangle
Write a function that takes the length and width of a rectangle and returns its area.
"""
def area_of_rectangle(length, width):
    return length * width

result = area_of_rectangle(5, 3)
print(result)
 
"""
Task 5: Celsius to Fahrenheit
Write a function that takes a temperature in Celsius and returns 
the equivalent temperature in Fahrenheit using the correct formula
"""
def  celsius_to_fashrenheit(celsius):
    return (celsius * 9/5) + 32

result = celsius_to_fashrenheit(25)
print(result)

"""
Task 6: Average of Numbers
Write a function that takes a list of numbers 
and returns the average (mean) of those numbers.
"""
def average(numbers):
    if not numbers:
        return 0 
"""
Task 7: Total Calculator
Create a function that has arguments for the price and quantity of something, and returns the total.
Your function should also optionally accept a 3rd argument for discount, and return the discounted if provided.
"""