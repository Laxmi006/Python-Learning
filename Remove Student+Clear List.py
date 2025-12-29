students = []

n = int(input("How many students do you want to add? "))

for i in range(n):
    name = input("Enter student name: ")
    students.append(name)

print("\nStudent list:", students)

#Remove student
remove_name = input("\nEnter student name to remove: ")

if remove_name in students:
    students.remove(remove_name)
    print("Student removed successfully")
else:
    print("student not found")

print("Updated Student List:", students)

#Clear list
clear_choice =input("\nDo you want to clear the student list? (yes/no): ")

if clear_choice.lower() == "yes":
    students.clear()
    print("Students list cleared")
print("Final Student List:", students)    

