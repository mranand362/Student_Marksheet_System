#student_Marksheet_system
schoolname =input("Enter your school name:- ")
session = int(input("Enter your session:- "))
rollno = int(input("Enter your roll no:- "))
name = input("Enter your name:- ")
fathername = input("Enter your father name:- ")
mothername = input("enter your mother name:- ")
standard = int(input("Enter class:- "))
physic = int(input("Enter physic marks:- "))
chemistry = int(input("Enter chemistry marks:- "))
math = int(input("Enter maths marks:- "))
english = int(input("Enter english marks:- "))
hindi = int(input("enter hindi marks:- "))
obtained_marks = physic+chemistry+math+english+hindi
print(obtained_marks)
percentage = obtained_marks/500*100
print(percentage)



print("----------student marksheet-----------")
print("session:-" +str(session))
print("your roll no is : " +str(rollno))
print("your name is: " +name)
print("your father name is:-" +fathername)
print("your mother name is:-" +mothername)
print("your class is: " +str(standard))
print("total marks are: 500 ")
print("obtained marks are: " +str(obtained_marks))
print("your percentage is: " +str(percentage))

if percentage >=80:
    print("grade: A+")
    print("Remarks : Excellent")
elif percentage>=70:
    print("grade: A")
    print("Remarks : Very Good ")
elif percentage >=60:
    print("grade: B")
    print("Remarks : Good")
elif percentage >=50:
    print("grade: C")
    print("Remarks : Poor")
elif percentage >=40:
    print("grade: D")
    print("Remarks : Needs Improvement")
elif percentage >=33:
    print("grade: E")
    print("Remarks : Failure")
i =0
if  physic <=33:
      i = i +1
if chemistry <= 33:
    i = i +1

if  math <=33:
    i = i+1

if  english <=33:
    i =i+1

if hindi <=33:
    i = i+1
print("Failed subject count: " + str(i))