# PyPassword Generator
# Create Password Generator Project

import random
print("Welcome to the PyPassword Generator!")
nb_letters = int(input("How many letters would you like in your password?\n"))
nb_symbols = int(input(f"How many symbols would you like?\n"))
nb_numbers = int(input(f"How many numbers would you like?\n"))

Letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"
           "A", "B", "C", "D", "E", "F", "G", "H", "I", "J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

Symbols = ["!","@","#","$","%","^","&","*","(",")","_","+"]
Numbers = ["0","1","2","3","4","5","6","7","8","9"]

password = []

for i in range(0,nb_letters +1):
    password.append(random.choice(Letters))

for i in range(0,nb_symbols +1):
    password.append(random.choice(Symbols))

for i in range(0,nb_numbers +1):
    password.append(random.choice(Numbers))
random.shuffle(password)
print(password)

# print("".join(password))

YourPassword = ""
for char in password:
    YourPassword += char
print(f"Your Password is: {YourPassword}")


