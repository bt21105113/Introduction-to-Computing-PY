#QUESTION 1
a=input("Enter first Number:") 
b=input("Enter second Number:")
c=input("Enter third Number:")

a=int(a)
b=int(b)
c=int(c)
avg=(a+b+c)/3 #writing the formula for finding average
print("The Average of three number is: ",(avg))


#QUESTION 2
Gross_Income=input("Enter the Gross Income: ")
Dependents=input("Enter the Number of Dependents: ")

a=int(Gross_Income)
b=int(Dependents)

taxrate=0.2
Standard_Deduction=10000
Dependent_deduction=3000

Taxable_Income=a-Standard_Deduction-(Dependent_deduction*b)
tax=Taxable_Income*taxrate
print("Income Tax is: ", tax)

#QUESTION 3
SID=int(input("Enter the SID:> "))
Name=str(input("Enter the Name:> "))
Gender=str(input("Enter the Gender:> "))
Course_Name=str(input("Enter the Course Name:> "))
CGPA=float(input("Enter the CGPA:> "))

Student=[]
Student.append(SID)
Student.append(Name)
Student.append(Gender)
Student.append(Course_Name)
Student.append(CGPA)
print(Student)


#QUESTION 4
#Taking the input of marks of 5 students from the user
a1=input("Enter the marks of Student 1: ")
a2=input("Enter the marks of Student 2: ")
a3=input("Enter the marks of Student 3: ")
a4=input("Enter the marks of Student 4: ")
a5=input("Enter the marks of Student 5: ")

SortedMarks=[a1,a2,a3,a4,a5]
SortedMarks.sort()

print("The Sorted List is; ",(SortedMarks))

#QUESTION 5_part A
List=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
del List[3]
print("The new list is: ",(List))

#QUESTION 5_part B
color=['Red','Green','White','Black','Pink','Yellow']
color[3:5]=['Purple']
print("The new list after replacing 'Black'&'Pink' with 'Purple' is: ",(color))




