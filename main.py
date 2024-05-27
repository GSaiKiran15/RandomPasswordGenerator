import random
import string

lower_letters = string.ascii_lowercase
upper_letters = string.ascii_uppercase
symbols = "~!`@#$%^&*/?><|"
numbers = "0123456789"

try:
    password_length = int(input("Enter the length of Password: "))
except ValueError:
    password_length = 8

password = ""
special_character = random.choice(symbols)
random_number = random.choice(numbers)

    