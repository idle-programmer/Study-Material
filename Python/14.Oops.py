# Class : Blueprint or template for creating objects
# Object: Instance of a class, anything in python can be considered as object of a class

# Inheritance: Allows a class to inherit properties and behaviors from an existing class (superclass) to new class (subclass)
"""
a. Single Inheritance - Simple ,Animal → Dog
b. Multiple Inheritance - Multiple are passed ,Mom + Dad → Child
c. Multilevel Inheritance - Y inherits X and then Z inherits Y ,Grandpa → Father → Son
d. Hierarchical Inheritance - Inherits from same super class , Vehicle → Car + Bike
"""
"""examples:"""
class LivingBeing:
    def __init__(self,name):
        self.name=name

class Human(LivingBeing):
    def speak(self):
        return f"{self.name} says Hello"

class Animal(LivingBeing):
    def speak(self):
        return f"{self.name} does not speak"
    
dog = Animal("Dog")
print(dog.speak())  # Output: Dog does not speak


class Model:
    @staticmethod
    def CharField(max_length=255):
        return f"CharField(max_length={max_length})"

    
class User(Model):
    name = Model.CharField(max_length=50)

user1 = User()
print(user1.name)  # Output: CharField(max_length=50)

# Encapsulation: Bundling data and methods that operate on that data with in a single unit or class
class User:
    def __init__(self,name):
        self.__name=name.upper()  # private attribute

    def get_name(self):
        return self.__name

user = User("Mehul")
print(user.get_name())

# Abstraction : Hides implementations details and shows only essential features
from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self):
        # some payment logic is implemented
        pass

class UPI(Payment):
    def pay(self):
        return "Payment done using UPI"
    
upi=UPI()
print(upi.pay())

# Polimorphism: allows the same method name to have different behaviours based on the object.
class Cat:
    def sound(self):
        return "Meow"

class Dog:
    def sound(self):
        return "Bark"

def animal_sound(animal):
    return animal.sound()   

cat = Cat()
print(animal_sound(cat))

# Interview Questions
# Goal/Benefits of using oops
"""
OOP helps us write code that is reusable, maintainable, 
scalable and closer to real world scenarios.
"""

#What is method? Different types of methods in python?
"""
Methods are functions defined inside a class. They can be:
1. Instance methods - operate on instance data
2. Class methods - operate on class data (use @classmethod decorator)
3. Static methods - operate independently of class or instance (use @staticmethod decorator)
"""
class Student:
    school = "ABC School"
    def __init__(self, name):
        self.name = name 
    
    def show(self):
        print(f"{self.name}")

    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school

    @staticmethod
    def is_teenager(age):
        return 13 <= age <= 19


# What is instance?
"""
An instance is an object from a class that represents a real-world entity in memory.
An instance is an individual object created from a class.
Each instance has its own attributes and can call the methods defined in the class.
"""
# ⁠What is self in python?
"""
self refers to the instance of the class itself. It is used to access variables and methods associated with that specific instance.
"""

# What are dunder/magic methods?
"""Methods in Python that start and end with double underscores (e.g., __init__, __str__). 
They are used to define special behaviors for objects.
Examples:
1. __init__: Constructor method to initialize an object.
2. __str__: Defines string representation of an object.
3. __add__: Defines behavior for the + operator.
4. __len__: Defines behavior for the len() function.
5.__iter__: Returns an iterator object for iteration."""

# What is MRO?
"""Method Resolution Order (MRO) is the order in which Python looks for a method in a hierarchy of classes."""
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(B):
    def show(self):
        print("C")

class D(C, B):
    pass

D().show() # (D, C, B, A, object)

# What is monkey patching?
"""
Monkey patching is a programming technique used to dynamically
modify or extend the behaviour of class, module, or function at 
runtime without altering its original code.

# original_module.py
class MyClass:
    def say_hello(self):
        return "Hello, Welcome to the original class!"

# main_script.py
from original_module import MyClass

def new_say_hello(self):
    return "Greetings! The class has been monkey patched!"

MyClass.say_hello = new_say_hello
obj = MyClass()
print(obj.say_hello()) # output = Greetings! The class has been monkey patched!


| #                   | Monkey Patching           | Decorator                                   |
| ------------------- | ------------------------- | ------------------------------------------- |
| 1. Timing           | Applied at runtime        | Applied at definition time                  |
| 2. Mechanism        | Class.method = new_method | function/class as an argument, @ syntax     |
| 3. Scope            | global change             | impacts only the specific function or class |
"""

# What is a metaclass in Python?
"""
A metaclass is the "class of a class" that customizes how other classes are created. Every class in Python 
is an instance of a metaclass—by default, it's the built-in type. You create one by subclassing type and 
overriding methods like __new__(cls, name, bases, attrs), which receives the class name, base classes, and 
attributes dictionary. This allows injecting behavior, like auto-registering classes or validating attributes.
"""