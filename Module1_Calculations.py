# This is the first assignment - Module1.
# Title:  Module1_Calculations.py
# Description: This program performs calculations (addition, subtraction, multiplication, and division)
#           on two numbers provided by the user. The program is divided into two parts:
#           Part 1 handles addition and subtraction, while Part 2 handles multiplication and division.
#           Added in error handling for division by zero.  Used FLOAT for user inputs to allow decimal numbers.
#           The results of each operation are displayed to the user.


# Ask the user to enter two numbers
# Using FLOAT instead of INT to allow decimal inputs (error will occur if the user inputs non-numeric values or decimals when using INT)
print("\n")
print('You will be asked to enter two numbers for addition and subtraction.')
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Part 1: Add and subtract
add = num1 + num2
subtract = num1 - num2
print("\n")
print("Part 1: Add and Subtract Results")
print("Addition results (first number + second number):", add)
print("Subtraction results (first number - second number):", subtract)
print("\n")
# Part 2: Multiply and divide
# Since Part 2 is separate, we will ask the user to enter two new numbers.
# Left the original variable names as num1 and num2 for Part 1, and used num3 and num4 for Part 2.
# This would allow me to use num1 and num2 again if needed without overwriting the values from Part 1.
print('You will now be asked to enter two numbers for multiplication and division.')
num3 = float(input("Enter the first number: "))
num4 = float(input("Enter the second number: "))

multiply = num3 * num4
print("\n")
print("Part 2: Multiply and Divide")
print("Multiplication results (first number * second number):", multiply)

# Had to add this to check if the user entered zero for the second number to avoid division by zero.
if num4 != 0:
    divide = num3 / num4
    print("Division results (first number / second number):", divide)
else:
    print("Division results (first number / second number): You entered a zero and you cannot divide by zero.")
print("\n")
print("End of Module 1 Calculations Program.")
