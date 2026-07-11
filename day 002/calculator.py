print("Welcome to the Tip Calculator!")

# Asking for the bill
bill = float(input("What was your total bill? $"))

# Asking for the tip percentage
tip = float(input("How much tip would you like to give? 10, 12, or 15? "))

# Calculating the total bill with the tip
tip_amount = tip * bill / 100
total_bill = bill + tip_amount

# Asking for the number of people
people = float(input("How many people to split the bill? "))

# Calculating the price per person
per_person = round(total_bill / people, 2)

print(f"Each person should pay: ${per_person}")