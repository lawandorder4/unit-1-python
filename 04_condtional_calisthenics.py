'''
Exercise 1:
Check if an integer is even and greater than 10.
Return True if both conditions are met, False otherwise.
'''
n = int(input("type a number:"))
if n >= 18 
'''
Exercise 2:
Determine the ticket price based on age and student status.
Price is $10 if under 18 or a student, $20 otherwise.
'''
def determine_ticket_price(age, is_student):

    if age < 0:
        return "Error: Age cannot be negative."
    
    if age < 18 or is_student:
        price = 10
    else:
        price = 20 

        return f"the ticket price is ${price}."
    
    age = 16 
    is_student = True
    result = determine_ticket_price(age, is_student)
    print(result)
    

'''
Exercise 3:
Prompt the user to enter a fruit name. Check if the fruit is in the list. 
If it is, print "Yes, that fruit is in the list." 
If it's not, print "No, that fruit is not in the list."
'''
def check_fruit_in_list

fruit_list = []

'''
Exercise 4:
Check if a year is a century year and a leap year.
'''

'''
Exercise 5:
Calculate the cost of shipping for an online order based on the order weight and destination zone. 
The shipping cost is $5 per kilogram for Zone A and $7 per kilogram for Zone B. 
If the order weight is less than 0 kg, return an error message.
'''
#checking for invalid weights in the order 
def calculate_hipping_cost(weight, zone):
    if weight < 0:
    return "Error: weight can not be lesss then 0 kg"
#im defining the shipping rates 
rates = {
    
    'A': 5,
    'b': 7
}

if zone not in rates: 
    return "Error: invalid destination zone."


cost = weight * rates[zone]
return f"The shipping cost is ${cost:.2f}."



order_weight = 10
destination_zone = 'A'
result = calculate_hipping_cost(order_weight, destination_zone)
print(result)

'''
Exercise 6:
Determine the type of a triangle based on side lengths.
Equilateral, Isosceles, Scalene, or Not a triangle.
'''