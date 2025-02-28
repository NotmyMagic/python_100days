import random

upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', "i", 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%' ,'&', ',', '*', '+']
set_password = []

# added = 0
# for number in range(1, 101):
#     added += number

# print(added)

set_up_letters = int(input("How many capital letters would you like in your password?\n"))
set_low_letters = int(input("How many lowercase letters would you like in your password?\n"))
set_numbers = int(input("How many numbers would you like in your password?\n"))
set_symbols = int(input("How many symbols would you like in your password?\n"))


for choice in range(0, set_up_letters):
    set_password.append(random.choice(upper))

for choice in range(0, set_low_letters):
    set_password.append(random.choice(lower))

for choice in range(0, set_numbers):
    set_password.append(random.choice(numbers))

for choice in range(0, set_symbols):
    set_password.append(random.choice(symbols))

random.shuffle(set_password)
password = "".join(set_password)

# print(set_password)

print(password)