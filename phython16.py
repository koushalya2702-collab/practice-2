#Exception Handling in Python
try:
    age = int(input("Enter your age: "))

    if age < 0:
        raise ValueError("Age cannot be negative!")

except ValueError as e:
    print("Invalid input:", e)

else:
    years_left = 100 - age
    print(f"You will be 100 years old in {years_left} years.")

finally:
    print("Program finished.")


#Safe Divider
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = num1 / num2

except ValueError:
    print("Invalid input! Please enter numbers only.")

except ZeroDivisionError:
    print("Cannot divide by zero!")

else:
    print("Result is:", result)

finally:
    print("Program finished.")