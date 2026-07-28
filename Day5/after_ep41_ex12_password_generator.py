import string
import random

print("Welcome to the password generator!")
letters = string.ascii_letters
numbers = string.digits
special_characters = string.punctuation

nr_letters = int(input("How many letters you want in your password? "))
nr_numbers = int(input("How many numbers you want in your password? "))
nr_special_characters = int(input("How many special characters you want in your password? "))

password_list = []

for char in range(0, nr_letters):
    password_list.append(random.choice(letters))

for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

for char in range(0, nr_special_characters):
    password_list.append(random.choice(special_characters))

random.shuffle(password_list)

password = ""

for char in password_list:
    password += char

print("Your password is: ", password)