def get_input():
    print("Welcome to the tip calculator")
    total = float(input("What was the total bill? "))
    percentage = float(input("What percentage tip would you like to give? 10, 12, or 15>? "))
    people = int(input("How many people to split the bill? "))

    tip = total//100 
    total_payment = total + tip
    payment = total_payment // people

    print("Each person should pay:", payment)


get_input()
