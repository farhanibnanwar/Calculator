# Bismillah Hir-Rahman Nir-Rahim.
# Basic calculator with minimal features
# without graphical interface.

first_number = input("Write first number: ")
second_number = input("Write second number: ")
operation = input("Input operation +, -, *, /: ")

# Convert strings to integers.
first_number = int(first_number)
second_number = int(second_number)

# Define operations.
if operation == "+":
    result = first_number + second_number
elif operation == "-":
    result = first_number - second_number
elif operation == "*":
    result = first_number * second_number
elif operation == "/":
    result = first_number / second_number
else:
    print("Enter a valid operation.")

print(result)
