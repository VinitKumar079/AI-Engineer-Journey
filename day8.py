# ==========================================
# AI Engineer Journey
# Official Day 8
# Topic : Exception Handling
# Author : Vinit Kumar
# ==========================================

print("========== EXCEPTION HANDLING ==========\n")


# 1. Basic try-except

try:
    number = int(input("Enter a number: "))
    print("You entered:", number)

except ValueError:
    print("Please enter a valid number.")


# 2. Division Error

try:
    a = int(input("\nEnter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

    print("Result:", result)

except ValueError:
    print("Please enter numbers only.")

except ZeroDivisionError:
    print("You cannot divide by zero.")


# 3. try-except-else

try:
    age = int(input("\nEnter your age: "))

except ValueError:
    print("Invalid age.")

else:
    print("Your age is:", age)


# 4. finally

try:
    print("\nTrying some code...")

except:
    print("Something went wrong.")

finally:
    print("This block always runs.")


# 5. Multiple Errors

try:
    number = int(input("\nEnter a number: "))
    result = 100 / number

    print("100 /", number, "=", result)

except ValueError:
    print("Invalid input.")

except ZeroDivisionError:
    print("Cannot divide by zero.")


# 6. raise

try:
    age = int(input("\nEnter your age: "))

    if age < 0:
        raise ValueError("Age cannot be negative.")

    print("Valid age:", age)

except ValueError as error:
    print("Error:", error)


print("\nDay 8 Completed Successfully 🚀")