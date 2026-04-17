#File Handling in Python
file=open("data.txt","r")
content=file.readlines()
print(content)
file.close()


#Writing to a File
file=open("notes.txt","w")
file.write("Namaskara Bengaluru\n")
file.close()

#Appending to a File
file=open("notes.txt","a")
file.write("\n Namaskara karnataka\n")
file.close()


# Using with Statement 
with open("data.txt","r") as file:
    content=file.read()
    print(content)


#Writing List of Data to File
students=["koushalya","kanaka","manjula","prema"]
with open("student.txt","w") as file:
    for student in students:
        file.write(student + "\n" )

# Reading File and Processing Each Line
with open("students.txt", "r") as file:
    for line in file:
        print("Student:", line.strip())



# Homework
#Create a File and Write
friends=["naveen","adi","pavan"]
with open("friends.txt","w") as file:
    for friend in friends:
        file.write(friend +"\n")

#Append Marks  
name = input("Enter student name: ")
marks = input("Enter marks: ")

with open("marks.txt","a") as file:
    file.write(name + " - " + marks + "\n")
print("Data saved successfully!")



#Read and Count Lines
count=0
with open("student.txt","r") as file:
    for line in file:
        count+=1
print("Total students:", count)


#Search From File

name = input("Enter name: ")

with open("friends.txt", "r") as file:
    data = file.read()

if name in data:
    print("Found!")
else:
    print("Not Found!")