#Function
#Basic function to greet a user
def greet():
    print("Hey,welcome")
greet()

#Function Parameters
def greet(name):
    print(f"hello {name}")
greet("koushalya")


#Returning Values from a Function
def add(a,b):
    return a+b
sum=add(3,5)
print("The sum is:",sum)

#Default Parameter Values
def greet(name="koushalya"):
    print(f"Hey {name} welcome back")
greet()
greet("kamali")