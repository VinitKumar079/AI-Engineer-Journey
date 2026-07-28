# ==========================================
# AI Engineer Journey
# Official Day 7
# Topic : File Handling
# Author : Vinit Kumar
# ==========================================

print("========== FILE HANDLING ==========\n")

# Create & Write
file = open("student.txt", "w")

file.write("Name : Vinit\n")
file.write("Course : AI Engineering\n")
file.write("Language : Python\n")

file.close()

print("Data Written Successfully")

# Read File
file = open("student.txt", "r")

content = file.read()

print("\nFile Content\n")
print(content)

file.close()

# Append Data
file = open("student.txt", "a")

file.write("College : IPEC\n")

file.close()

print("New Data Added")

# Read Again
file = open("student.txt", "r")

print("\nUpdated File\n")
print(file.read())

file.close()

print("\nDay 7 Completed 🚀")