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
    
dog = Human("Dog")
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
        self.__name=name  # private attribute

    def get_name(self):
        return self.__name

user = User("Mehul")
print(user.get_name())

# Abstraction : Hides implementations details and shows only essential features
from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self):
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