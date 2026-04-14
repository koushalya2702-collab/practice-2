#Conditional Statements in Python: if, elif, and else

time = 18
if time == 13:
    print("Its time for lunch")
elif time == 18:
    print("Its time for snacks")
elif time == 20:
    print("Its time for dinner")
else:
    print("Its not meal time")

#Comparison Operators in if Statements
age = 19

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

#Nested if statement
day = input("Enter a day: ")
is_raining=False

if day == "saturday" or day== "sunday":
    if not is_raining:
        print("Lets visit a mysuru")
    else:
        print("Its raining, lets stay home")
else:
    print("Its a weekday,wait for weekend")


    
#Simple Eligibility Check
age = int(input("Enter your age"))
if age < 18:
    print("You get a  student membership")
elif age >= 60:
    print("You may get a senior citizen membership")
else:
    print("You get a regular membership")



#match-case
day = "Sunday"

match day:
    case "Monday":
        print("Start of the work week.")
    case "Friday":
        print("Almost weekend!")
    case "Saturday" | "Sunday":
        print("It's the weekend!")
    case _:
        print("Just another weekday.")


#Checking Bus Ticket Prices
age = 65

if age < 5:
    print("Ticket is free.")
elif age <= 12:
    print("You get a child discount.")
elif age >= 60:
    print("You get a senior citizen discount.")
else:
    print("You pay the full fare.")