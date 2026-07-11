print("Welcome to the rollercoaster! :)")

height = int(input("Enter your height in cm: "))

if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("How old are you? "))

    if age < 12:
        print("Your ticket costs $5.")
        ticket = 5

    elif age <= 18:
        print("Your ticket costs $7.")
        ticket = 7

    elif age >= 45 and age <= 55:
        print("everything is going to be ok. Have a free ride on us!")

    else:
        print("Your ticket costs $12.")
        ticket = 12

    photo = input("Do you want to buy a photo? (Y/N): ")

    if photo == "Y":
        ticket += 3

    print(f"Your total ticket price is ${ticket}.")

else:
    print("You can't ride the rollercoaster.")