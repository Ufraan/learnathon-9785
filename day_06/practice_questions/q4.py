"""
Write a Python program that determines the price of a movie ticket based on the age and time of the show. 
The program should take the age and time (in 24-hour format) as inputs and use the `match` statement to calculate 
and print the ticket price according to the following rules:

- For age 0-5, the ticket is free.
- For age 6-12, the ticket is $10.
- For age 13-18, the ticket is $15.
- For age 19 and above, the ticket is $20.
- For shows before 12:00 PM, there is a $5 discount on the ticket.
"""


age = int(input("Enter  age: "))
show_time = int(input("Enter  show time (in 24-hour format): "))

match age:
    case 0 | 1 | 2 | 3 | 4 | 5:
       ticket_price =  0
    case 6 | 7 | 8 | 9 | 10 | 11 | 12:
       ticket_price =  10
    case 13 | 14 | 15 | 16 | 17 | 18:
       ticket_price =  15
    case _:
       ticket_price =  20 

if show_time < 12:
    ticket_price -= 5

print(f"The ticket price is ${ticket_price}.")
