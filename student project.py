class Student:
    def __init__(self, name, age, course, marks):
       self.name=name
       self.age=age
       self.course=course
       self.marks=marks
    def display(self):
        print(self.name)
        print(self.age)
        print(self.course)
        print(self.marks)
students=[]
while True:
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Delete student")
    print("5. Update the student details")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice==1:
       name=input("Enter the student name:")
       age=int(input("enter the age:"))
       course=input("enter the course:")
       marks=int(input("enter the marks:"))
       new_student=student(name,age,course,marks)
       students.append(new_student)
    elif choice==2:
        for student in students:
            student.display()
    elif choice==3:
        search_name=input("enter the student name to search:")
        found=False
        for student in students:
           if student.name==search_name:
              student.display()
              found=True
        if found==False:
            print("student details not found")
    elif choice==4:
        found=False
        delete_name=input("Enter the whichu student name do you  remove:")
        for student in students:
            if  student.name==delete_name:
                students.remove(student)
                print("Delete student sucessfully")
                found=True
                break
        if found==False:
            print("Student details not found:")

    elif choice==5:
        update_details=input("Enter the student name to updated:")
        found= False
        for student in students:
            if student.name==update_details:
                print("1.name update:")
                print("2.age update:")
                print("3.course update:")
                print("4.marks update:")
                update=int(input("whic one do you want update:"))
                if update==1:
                    student.name=input("Enter the name:")
                elif update==2:
                    student.age=int(input("Enter the update age:"))
                elif update==3:
                    student.course=input("enter the ypdated course name:")
                elif update==4:
                    student.marks=int(input("Enter the updated marks:"))
                print("student details sucessfully updated")
                found=True
        if found==False:
            print("student details not found")
    elif choice==6:
        break
