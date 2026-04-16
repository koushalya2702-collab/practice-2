#Using self in Class Methods
class Person:
    def __init__(self, name, age):
        self.name = name  # 'self.name' is an instance variable
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

# Creating an object
person1 = Person("Arjun", 22)
person1.introduce()

#Creating Multiple Objects with Different Attributes
class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def show_info(self):
        print(f"Laptop Brand: {self.brand}, Price: ₹{self.price}")

laptop1 = Laptop("Dell", 45000)
laptop2 = Laptop("HP", 55000)

laptop1.show_info()
laptop2.show_info()

#Optional Parameters in Constructors
class Book:
    def __init__(self, title, author="Unknown"):
        self.title = title
        self.author = author

    def show_book(self):
        print(f"Title: {self.title}, Author: {self.author}")

book1 = Book("Python Programming")
book2 = Book("Machine Learning", "Andrew Ng")

book1.show_book()
book2.show_book()