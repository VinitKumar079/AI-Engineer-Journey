# ==========================================
# AI Engineer Journey
# Official Day 11
# Topic: OOP Advanced
# Author: Vinit Kumar
# ==========================================


# ==========================================
# 1. ENCAPSULATION
# ==========================================

class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount deposited successfully.")
        else:
            print("Invalid amount.")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Amount withdrawn successfully.")
        else:
            print("Insufficient balance.")

    def get_balance(self):
        return self.__balance


account = BankAccount("Vinit", 5000)

print("========== ENCAPSULATION ==========")

print("Name:", account.name)
print("Balance:", account.get_balance())

account.deposit(2000)

print("Balance:", account.get_balance())

account.withdraw(1000)

print("Balance:", account.get_balance())


# ==========================================
# 2. INHERITANCE
# ==========================================

class Animal:

    def eat(self):
        print("Animal is eating.")


class Dog(Animal):

    def bark(self):
        print("Dog is barking.")


dog = Dog()

print("\n========== INHERITANCE ==========")

dog.eat()
dog.bark()


# ==========================================
# 3. METHOD OVERRIDING
# ==========================================

class Vehicle:

    def start(self):
        print("Vehicle is starting.")


class Car(Vehicle):

    def start(self):
        print("Car is starting with a button.")


car = Car()

print("\n========== METHOD OVERRIDING ==========")

car.start()


# ==========================================
# 4. POLYMORPHISM
# ==========================================

class Cat:

    def sound(self):
        print("Cat says Meow.")


class Dog2:

    def sound(self):
        print("Dog says Woof.")


class Cow:

    def sound(self):
        print("Cow says Moo.")


animals = [Cat(), Dog2(), Cow()]

print("\n========== POLYMORPHISM ==========")

for animal in animals:
    animal.sound()


# ==========================================
# 5. AI MODEL EXAMPLE
# ==========================================

class AIModel:

    def predict(self):
        print("AI Model is making a prediction.")


class MLModel(AIModel):

    def predict(self):
        print("Machine Learning model is predicting.")


class DeepLearningModel(AIModel):

    def predict(self):
        print("Deep Learning model is predicting.")


models = [MLModel(), DeepLearningModel()]

print("\n========== AI MODEL POLYMORPHISM ==========")

for model in models:
    model.predict()


print("\nDay 11 Completed Successfully 🚀") 

#########################################################
# ==========================================
# AI Engineer Journey
# Official Day 12
# Topic: OOP Mini Project - AI Model Manager
# Author: Vinit Kumar
# ==========================================


class AIModel:

    def __init__(self, name, accuracy):
        self.name = name
        self.accuracy = accuracy

    def display_info(self):
        print(f"Model Name : {self.name}")
        print(f"Accuracy   : {self.accuracy}%")

    def predict(self):
        print(f"{self.name} is making a prediction...")


class MLModel(AIModel):

    def predict(self):
        print(f"{self.name} is making an ML prediction.")


class DeepLearningModel(AIModel):

    def predict(self):
        print(f"{self.name} is making a Deep Learning prediction.")


# Creating objects

model1 = MLModel("Random Forest", 92)
model2 = DeepLearningModel("Neural Network", 96)


print("========== AI MODEL 1 ==========")

model1.display_info()
model1.predict()


print("\n========== AI MODEL 2 ==========")

model2.display_info()
model2.predict()


# Polymorphism

models = [model1, model2]

print("\n========== ALL MODELS ==========")

for model in models:
    model.predict()


# Simple Model Comparison

print("\n========== MODEL COMPARISON ==========")

if model1.accuracy > model2.accuracy:
    print(model1.name, "has higher accuracy.")
elif model2.accuracy > model1.accuracy:
    print(model2.name, "has higher accuracy.")
else:
    print("Both models have the same accuracy.")


print("\nDay 12 Completed Successfully 🚀")

###################################################

# ==========================================
# AI Engineer Journey
# Official Day 13
# Topic: Advanced Collections
# ==========================================

print("========== LIST COMPREHENSION ==========\n")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = [number * number for number in numbers]

print("Numbers:", numbers)
print("Squares:", squares)


even_numbers = [number for number in numbers if number % 2 == 0]

print("Even Numbers:", even_numbers)


print("\n========== DICTIONARY COMPREHENSION ==========\n")

students = ["Vinit", "Rahul", "Aman"]

student_lengths = {
    student: len(student)
    for student in students
}

print(student_lengths)


print("\n========== SET OPERATIONS ==========\n")

python_students = {"Vinit", "Rahul", "Aman"}
ai_students = {"Vinit", "Aman", "Rohit"}

print("Both Courses:", python_students & ai_students)

print("All Students:", python_students | ai_students)

print("Only Python:", python_students - ai_students)

print("\n========== NESTED DICTIONARY ==========\n")

models = {
    "model1": {
        "name": "Random Forest",
        "accuracy": 92
    },
    "model2": {
        "name": "Neural Network",
        "accuracy": 96
    }
}

for key, model in models.items():

    print("\nModel:", key)
    print("Name:", model["name"])
    print("Accuracy:", model["accuracy"])


print("\n========== FILTERING DATA ==========\n")

model_data = [
    {"name": "Random Forest", "accuracy": 92},
    {"name": "SVM", "accuracy": 87},
    {"name": "Neural Network", "accuracy": 96},
    {"name": "Decision Tree", "accuracy": 89}
]

high_accuracy_models = [
    model
    for model in model_data
    if model["accuracy"] >= 90
]

print("Models with 90%+ accuracy:")

for model in high_accuracy_models:
    print(model["name"], "-", model["accuracy"], "%")


print("\nDay 13 Completed Successfully 🚀") 