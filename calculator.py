a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice: "))

if choice == 1:
    result = a + b
    print("Result =", result)

elif choice == 2:
    result = a - b
    print("Result =", result)

elif choice == 3:
    result = a * b
    print("Result =", result)

elif choice == 4:
    if b != 0:
        result = a / b
        print("Result =", result)
    else:
        print("Division by zero is not possible")

else:
    print("Wrong choice")