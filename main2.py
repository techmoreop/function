a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
def add():
    return a + b
def subtract():
    return a - b
def multiply():
    return a * b
def divide():
    return a / b
print("Which operation you want to perform?")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = int(input("Enter choice(1/2/3/4): "))
if choice == 1:
    print(add())
elif choice == 2:
    print(subtract())
elif choice == 3:
    print(multiply())
elif choice == 4:
    print(divide())
else:
    print("Invalid input")