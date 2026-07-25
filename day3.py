# ==========================================
# AI Engineer Journey
# Official Day 3
# Topic : Loops (for & while)
# Author : Vinit Kumar
# ==========================================

print("========== FOR LOOP ==========\n")

# Print numbers 1 to 10

for i in range(1, 11):
    print(i)

print("\n========== TABLE ==========\n")

number = int(input("Enter a number: "))

for i in range(1, 11):
    print(number, "x", i, "=", number * i)

print("\n========== SUM ==========\n")

sum = 0

for i in range(1, 11):
    sum += i

print("Sum =", sum)

print("\n========== EVEN NUMBERS ==========\n")

for i in range(2, 21, 2):
    print(i)

print("\n========== ODD NUMBERS ==========\n")

for i in range(1, 21, 2):
    print(i)

print("\n========== WHILE LOOP ==========\n")

count = 1

while count <= 10:
    print(count)
    count += 1

print("\n========== FACTORIAL ==========\n")

num = int(input("Enter a number: "))

fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial =", fact)

print("\n========== PATTERN ==========\n")

for i in range(1, 6):
    print("*" * i)

print("\n========== DAY 3 COMPLETED ==========")

# ==========================================
# AI Engineer Journey
# Official Day 6
# Topic : Tuple, Set & Dictionary
# ==========================================

print("========== TUPLE ==========")

colors = ("Red", "Green", "Blue")

print(colors)
print(colors[1])

print("\n========== SET ==========")

numbers = {10, 20, 20, 30, 40, 40}

print(numbers)

numbers.add(100)

print(numbers)

numbers.remove(20)

print(numbers)

print("\n========== DICTIONARY ==========")

student = {
    "name": "Vinit",
    "age": 20,
    "course": "AI Engineering"
}

print(student)

print(student["name"])

student["city"] = "Delhi"

print(student)

print("\nKeys")

for key in student:
    print(key)

print("\nValues")

for value in student.values():
    print(value)

print("\nKey & Value")

for key, value in student.items():
    print(key, ":", value)

print("\nDay 6 Completed 🚀")

# ==========================================
# AI Engineer Journey
# Official Day 6
# Topic : Tuple, Set & Dictionary
# ==========================================

print("========== TUPLE ==========")

colors = ("Red", "Green", "Blue")

print(colors)
print(colors[1])

print("\n========== SET ==========")

numbers = {10, 20, 20, 30, 40, 40}

print(numbers)

numbers.add(100)

print(numbers)

numbers.remove(20)

print(numbers)

print("\n========== DICTIONARY ==========")

student = {
    "name": "Vinit",
    "age": 20,
    "course": "AI Engineering"
}

print(student)

print(student["name"])

student["city"] = "Delhi"

print(student)

print("\nKeys")

for key in student:
    print(key)

print("\nValues")

for value in student.values():
    print(value)

print("\nKey & Value")

for key, value in student.items():
    print(key, ":", value)

print("\nDay 6 Completed 🚀")