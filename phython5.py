#loop
i=1
while i<=5:
    print(i)
    i+=1

#Using break to Exit a while Loop
count=1
while count <= 10:
    if count == 5:
        print("Thats enough counting")
        break
    count+=1

#Using continue to Skip an Iteration
count=1
while count <= 10:
    if count == 5:
       count+=1
       continue
    print(f"count {count}")
    count+=1

#Basic Counting with while Loop:
i=1
while i <= 10:
    print(i)
    i+=1


#Using while Loops for User Input
pin = ""
correct_pin = "1234"
while pin != correct_pin:
    pin = input("Enter your PIN: ")
    if pin != correct_pin:
        print("Incorrect PIN. Try again.")
print("PIN accepted. You can proceed.")

#Real-life Example
available_seats = 5
while available_seats > 0:
    print(f"{available_seats} seats are available")
    book = input("Do you want to book a seat? (yes/no): ").lower()
    if book == "yes":
        available_seats -= 1
        print("Seat booked!")
    else:
        print("No booking mode")
print("All seats are booked")

#Odd Numbers Printer:
i=1
while i <= 20:
    if i%2 !=0:
        print(i)
    i += 1

#Countdown Timer:
i = 10
while i >= 1:
    print(i)
    i -= 1
print("Happy new year")