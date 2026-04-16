#OOP Concepts & Classes/Objects
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def display_info(self):
        print(f"Car brand:{self.brand},Model:{self.model}")
my_car = Car("BMW","corolla")
my_car.display_info()

#Attributes (Instance Variables) and Methods
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        print(f"hello i am {self.name} ,i am {self.age} years old")
person1=Person("koushalya",18)
person1.greet()

#Creating Multiple Objects from a Class
class Dog:
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed
    def bark(self):
        print(f"{self.name} is barking")
dog1=Dog("rex","golden retriver")
dog2=Dog("bolt","beagle")
dog1.bark()
dog2.bark()

#Homework
class Mobile:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def display(self):
        print(f"brand:{self.brand} , price:{self.price}")
mobile1=Mobile("Apple",80000)
mobile2=Mobile("Redmi9",10000)
mobile1.display()
mobile2.display()

#Method Definition:
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display_info(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("-------------------")
student1 = Student("Koushalya", 85)
student2 = Student("Rahul", 90)
student3 = Student("Anita", 78)
student1.display_info()
student2.display_info()
student3.display_info()