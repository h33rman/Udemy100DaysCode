"""
You are going to write a program that automatically prints the solution to the FizzBuzz game.
Your program should print each number from 1 to 100 in turn."""

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz") 
    elif i % 3 == 0:
        print("Fizz") 
    elif i % 5 == 0:
        print("Buzz") 
    else:
        print(i)
        