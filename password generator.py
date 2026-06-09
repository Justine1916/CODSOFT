import random

length = int(input("Enter password length: "))

chars = ""

print("Select characters for password")
print("1. Letters")
print("2. Numbers")
print("3. Special Characters")
print("4. Generate Password")

while True:
    ch = int(input("Enter choice: "))

    if ch == 1:
        chars += "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    elif ch == 2:
        chars += "0123456789"

    elif ch == 3:
        chars += "!@#$%^&*()_+-="

    elif ch == 4:
        break

    else:
        print("Invalid choice")

password = ""

for i in range(length):
    password += random.choice(chars)

print("Generated Password:", password)
