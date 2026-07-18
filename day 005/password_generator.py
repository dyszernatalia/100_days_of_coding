import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# easy version
password_list = []

for _ in range(nr_letters):
    random_letter = random.choice(letters)
    password_list.append(random_letter)

for _ in range(nr_symbols):
    random_symbol = random.choice(symbols)
    password_list.append(random_symbol)

for _ in range(nr_numbers):
    random_number = random.choice(numbers)
    password_list.append(random_number)

password = "".join(password_list)
print(f"easy password is: {password}")

# hard version
hard_pass_list = []

# without using function
password_list_for_ver_2 = password_list.copy()

for _ in range(0, len(password_list)):
    rand = random.choice(password_list)
    hard_pass_list.append(rand)
    password_list.remove(rand)

hard_pass_ver1 = "".join(hard_pass_list)
print(f"hard password version 1 is: {hard_pass_ver1}")

# using the shuffle() function
random.shuffle(password_list_for_ver_2)
hard_pass_ver2 = "".join(password_list_for_ver_2)

print(f"hard password version 2 is: {hard_pass_ver2}")
