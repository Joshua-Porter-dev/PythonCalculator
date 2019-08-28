operation = input("Would you like to add, subtract, divide, or multiply? ")

num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))

def add(num1, num2):
    print(num1 + num2)

def subtract(num1, num2):
    print(num1 - num2)

def divide(num1, num2):
    print(num1 / num2)

def multiply(num1, num2):
    print(num1 * num2)

if operation == 'add':
    add(num1, num2)

if operation == 'subtract':
    subtract(num1, num2)

if operation == 'divide':
    divide(num1, num2)

if operation == 'multiply':
    multiply(num1, num2)
