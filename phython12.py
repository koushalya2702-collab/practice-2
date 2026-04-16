#The Four Pillars of OOP

#Encapsulation
class ATM:
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amount):
        self.__balance+=amount
        print(f"Deposited {amount},new balance:{self.__balance}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Insufficient balance")

atm = ATM(1000)
atm.deposit(500)
atm.withdraw(300)

#Example
class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password  

    def get_username(self):
        return self.username

    def check_password(self, password):
        return password == self.__password

user = User("dev_karnataka", "pass1234")
print(user.get_username())  
print(user.check_password("wrong_pass"))  
print(user.check_password("pass1234"))  


#Abstraction     
class Car:
    def start_engine(self):
        print("Engine started")

    def accelerate(self):
        print("Car accelerating")

    def brake(self):
        print("Car stopping")

car = Car()
car.start_engine()  
car.accelerate()
car.brake() 

#Example
class Database:
    def __init__(self):
        self.__storage = {}

    def save_data(self, key, value):
        self.__storage[key] = value
        print(f"Data saved for {key}")

    def get_data(self, key):
        return self.__storage.get(key, "No data found")

db = Database()
db.save_data("user_101", {"name": "Raj", "age": 30})
print(db.get_data("user_101"))



#Inheritance
class Family:
    def __init__(self,surname):
        self.surname=surname
class Child(Family):
    def __init__(self,surname,name):
        super().__init__(surname)
        self.name=name
child=Child("Gowda","Monika")
print(f"{child.name} {child.surname}")

#example
class User:
    def __init__(self,username):
        self.username=username

    def login(self):
        print(f"{self.username} logged in")

class Admin(User):
    def delete_user(self,user):
        print(f"Admin {self.username} deleted user {user}")

admin = Admin("karnataka_admin")
admin.login()  # Inherited from User
admin.delete_user("user_102")

# Polymorphism

class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Bark")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

animals = [Dog(), Cat()]
for animal in animals:
    animal.make_sound()