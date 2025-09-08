# Intentional bugs for testing

def add_numbers(a, b):
    # missing return statement
    sum = a + b

def divide_numbers(a, b):
    return a / b  # can throw ZeroDivisionError

def greet(name):
    print("Hello, " + Name)  # 'Name' should be 'name'

x = add_numbers(5, 7)
print("Sum:", x)

y = divide_numbers(10, 0)  # division by zero
print("Division Result:", y)

greet("Robin")
