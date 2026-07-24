# ===========================================
# AI Engineer Journey
# Day 2 - Variables & Data Types
# Author: Vinit Kumar
# ===========================================

print("========== Day 2 ==========")

# Integer
age = 20

# Float
cgpa = 8.75

# String
name = "Vinit Kumar"

# Boolean
is_student = True

print("\n----- Variables -----")
print("Name:", name)
print("Age:", age)
print("CGPA:", cgpa)
print("Student:", is_student)

print("\n----- Data Types -----")
print(type(age))
print(type(cgpa))
print(type(name))
print(type(is_student))

# Multiple Assignment
x, y, z = 10, 20, 30

print("\nMultiple Variables")
print(x)
print(y)
print(z)

# Same Value Assignment
a = b = c = 100

print("\nSame Value Assignment")
print(a)
print(b)
print(c)

# Type Conversion
num = "50"

print("\nType Conversion")
print("Before:", type(num))

num = int(num)

print("After:", type(num))
print("Value:", num)

# Input
student_name = input("\nEnter your name: ")
student_marks = float(input("Enter your marks: "))

print("\nResult")
print("Student:", student_name)
print("Marks:", student_marks)

print("\nCongratulations! Day 2 Completed 🚀")

#📚 Topic
# Input & Output
# Type Casting
# String Basics
# f-Strings (Industry Standard)
# ===========================================
# AI Engineer Journey
# Day 3 - Input, Output & Strings
# Author: Vinit Kumar
# ===========================================

print("========== Day 3 ==========")

# -------------------------------
# Taking Input
# -------------------------------

name = input("Enter your Name: ")
age = int(input("Enter your Age: "))
height = float(input("Enter your Height (in feet): "))

print("\n----- Your Details -----")
print("Name :", name)
print("Age :", age)
print("Height :", height)

# -------------------------------
# Type Casting
# -------------------------------

num1 = int(input("\nEnter First Number: "))
num2 = int(input("Enter Second Number: "))

print("\nAddition =", num1 + num2)
print("Subtraction =", num1 - num2)
print("Multiplication =", num1 * num2)
print("Division =", num1 / num2)

# -------------------------------
# String Operations
# -------------------------------

message = "Artificial Intelligence"

print("\nOriginal String :", message)
print("Upper Case :", message.upper())
print("Lower Case :", message.lower())
print("Length :", len(message))
print("Replace :", message.replace("Artificial", "Generative"))

# -------------------------------
# f-Strings
# -------------------------------

print(f"\nHello {name}, your age is {age}.")
print(f"Your height is {height} feet.")

# -------------------------------
# Mini AI Example
# -------------------------------

skill = input("\nWhich AI skill do you want to learn? ")

print(f"""
Great Choice!

{name}, if you learn {skill}
daily with consistency,
you can become an AI Engineer.

Keep Learning 🚀
""")

print("========== Day 3 Completed ==========")

# Topic
# Operators
# Comparison Operators
# Logical Operators
# Assignment Operators
# ===========================================
# AI Engineer Journey
# Day 4 - Operators
# ===========================================

print("========== Day 4 ==========")

a = 15
b = 4

print("\nArithmetic Operators")
print("Addition =", a + b)
print("Subtraction =", a - b)
print("Multiplication =", a * b)
print("Division =", a / b)
print("Floor Division =", a // b)
print("Modulus =", a % b)
print("Power =", a ** b)

print("\nComparison Operators")
print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

print("\nLogical Operators")

x = True
y = False

print(x and y)
print(x or y)
print(not x)

print("\nAssignment Operators")

num = 10
num += 5
print(num)

num *= 2
print(num)

print("\nDay 4 Completed 🚀")

# Topic
# if
# else
# elif
# Nested if

# ===========================================
# AI Engineer Journey
# Day 5 - If Else
# ===========================================

print("========== Day 5 ==========")

age = int(input("Enter your age: "))

if age >= 18:
    print("You can vote.")
else:
    print("You cannot vote.")

marks = int(input("\nEnter your marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Need Improvement")

number = int(input("\nEnter a number: "))

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

username = input("\nEnter Username: ")
password = input("Enter Password: ")

if username == "admin":
    if password == "1234":
        print("Login Successful")
    else:
        print("Wrong Password")
else:
    print("Invalid Username")

print("\nDay 5 Completed 🚀")