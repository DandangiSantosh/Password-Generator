import random

list_character = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
list_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
list_symbols = ['!', '@', '$', '%', '&', '*', '(', ')', '+', '#']

print("\nWelcome to password generator....\n")

n_letters = int(input("Enter number of letters you want in password: \n"))
n_numbers = int(input("Enter number of numbers you want in password: \n"))
n_symbols = int(input("Enter number of symbols you want in password: \n"))

pasword_list = []

for i in range(0,n_letters):
    char = random.choice(list_character)
    pasword_list += char

for i in range(0,n_numbers):
    char = random.choice(list_numbers)
    pasword_list += char

for i in range(0,n_symbols):
    char = random.choice(list_symbols)
    pasword_list += char

random.shuffle(pasword_list)
password = ""
for char in pasword_list:
    password += char

print("\nGenerated Password: ")
print(password)
