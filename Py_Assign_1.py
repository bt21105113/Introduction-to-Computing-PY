Python 3.9.9 (tags/v3.9.9:ccb0e6a, Nov 15 2021, 18:08:50) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=input("Enter first Number:")
Enter first Number:12
>>> b=input("Enter second Number:")
Enter second Number:3
>>> c=input("Enter third Number:")
Enter third Number:6
>>> a=int(a)
>>> b=int(b)
>>> c=int(c)
>>> avg=(a+b+c)/3
>>> print("The Average of three number is: ",(avg))
The Average of three number is:  7.0
>>> 
>>> #Question 2
>>> Gross_Income=input("Enter the Gross Income: ")
Enter the Gross Income: 20000
>>> Dependents=input("Enter the Number of Dependents: ")
Enter the Number of Dependents: 2
>>> a=int(Gross_Income)
>>> b=int(Dependents)
>>> taxrate=0.2
>>> Standard_Deduction=10000
>>> Dependent_deduction=3000
>>> Taxable_Income=a-Standard_Deduction-(Dependent_deduction*b)
>>> tax=Taxable_Income*taxrate
>>> print("Income Tax is: ", tax)
Income Tax is:  800.0
>>> 
>>> #Question 3
>>> SID=int(input("Enter the SID:> "))
Enter the SID:> 21105113
>>> Name=str(input("Enter the Name:> "))
Enter the Name:> Anjali
>>> Gender=str(input("Enter the Gender:> "))
Enter the Gender:> F
>>> Course_Name=str(input("Enter the Course Name:> "))
Enter the Course Name:> Intro to Computing
>>> CGPA=float(input("Enter the CGPA:> "))
Enter the CGPA:> 9.1
>>> Student=[]
>>> Student.append(SID)
>>> Student.append(Name)
>>> Student.append(Gender)
>>> Student.append(Course_Name)
>>> Student.append(CGPA)
>>> print(Student)
[21105113, 'Anjali', 'F', 'Intro to Computing', 9.1]
>>> 
>>> #Question 4
>>> a1=input("Enter the marks of Student 1: ")
Enter the marks of Student 1: 21
>>> a2=input("Enter the marks of Student 2: ")
Enter the marks of Student 2: 52
>>> a3=input("Enter the marks of Student 3: ")
Enter the marks of Student 3: 92
>>> a4=input("Enter the marks of Student 4: ")
Enter the marks of Student 4: 85
>>> a5=input("Enter the marks of Student 5: ")
Enter the marks of Student 5: 95
>>> SortedMarks=[a1,a2,a3,a4,a5]
>>> SortedMarks.sort()
>>> print("The Sorted List is; ",(SortedMarks))
The Sorted List is;  ['21', '52', '85', '92', '95']
>>> 
>>> #Question 5_(Part A)
>>> List=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
>>> del List[3]
>>> print("The new list is: ",(List))
The new list is:  ['Red', 'Green', 'White', 'Pink', 'Yellow']
>>> 
>>> #Question 5_(Part B)
>>> color=['Red','Green','White','Black','Pink','Yellow']
>>> color[3:5]=['Purple']
>>> print("The new list after replacing 'Black'&'Pink' with 'Purple' is: ",(color))
The new list after replacing 'Black'&'Pink' with 'Purple' is:  ['Red', 'Green', 'White', 'Purple', 'Yellow']
>>> 