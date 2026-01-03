students = int(input("Enter number of students: "))

marks = []

for i in range(students):
    mark = int(input(f"Enter marks of student{i+1}: "))
    marks.append(mark)

    print("All marks:", marks)

    print("Highest marks:", max(marks))
    print("Lowest marks:", min(marks))
    print("Average marks:", sum(marks) /len(marks))