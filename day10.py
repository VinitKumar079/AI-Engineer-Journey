# ==========================================
# AI Engineer Journey
# Official Day 10
# Topic : OOP - Classes & Objects
# Author : Vinit Kumar
# ==========================================

print("========== OOP IN PYTHON ==========\n")


# 1. Creating a Class

class Student:

    # Constructor
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    # Method
    def introduce(self):
        print(f"My name is {self.name}")
        print(f"My age is {self.age}")
        print(f"My course is {self.course}")


# 2. Creating Objects

student1 = Student("Vinit", 20, "AI Engineering")

student2 = Student("Rahul", 21, "Python")


# 3. Calling Methods

print("Student 1")
student1.introduce()

print("\nStudent 2")
student2.introduce()


# 4. Accessing Attributes

print("\n========== ATTRIBUTES ==========")

print("Name:", student1.name)
print("Age:", student1.age)
print("Course:", student1.course)


# 5. Another Class

class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):

        if b == 0:
            return "Cannot divide by zero"

        return a / b


calculator = Calculator()

print("\n========== CALCULATOR ==========")

print("Addition:", calculator.add(10, 5))
print("Subtraction:", calculator.subtract(10, 5))
print("Multiplication:", calculator.multiply(10, 5))
print("Division:", calculator.divide(10, 5))


print("\nDay 10 Completed Successfully 🚀")