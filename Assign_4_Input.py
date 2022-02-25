#QUESTION 1........................................................................

print("Question 1\n")
#Definig tower of Hanoi function
def tower_of_hanoi(n , source, destination, auxiliary):
    step_number=1
    if n==1:
        print ("Move disk 1 from",source,"to",destination)
        return
    tower_of_hanoi(n-1, source, auxiliary, destination)
    print ("Move disk",n,"from",source,"to",destination)
    tower_of_hanoi(n-1, auxiliary, destination, source)
    
#taking number of disk input from the user
no_of_disk=int(input("Enter number of disk in tower of Hanoi:"))
print("\nThe Disks are numbered starting from top of the tower."
      "\nSteps to move all disks from Source Tower to Destination Tower "
      "is given below:\n")
#Using the function of tower of hanoi
tower_of_hanoi(no_of_disk,"Source Tower","Destination","Auxiliary")

#Question 2........................................................................

print("\n[Question.2]\n")
#taking number of rows as input
row=int(input("Enter number of rows:"))
#forming central position for different number of rows
if row<=16:
    #forming fuction that will return next row of pascle triangle
    def psum(list1, row):
        i1 = 0
        i2 = 1
        l = []
        for i1 in range(row - 1):
            l.append(list1[i1] + list1[i2])
            i1 = i1 + 1
            i2 = i2 + 1
        l.insert(0, 1)
        l.append(1)
        return (l)

    #forming function that will print all rows using previous function
    def ptriangle(rows):
        if rows == 1:
            print(1)
        elif rows == 2:
            print(f" 1\n1 1")
        else:
            f = "{p:^90}".format(p=1)
            print(f)
            f = "{p:^90}".format(p="1  1")
            print(f)
            l1 = [1, 1]
            row = 2
            for i in range(rows - 2):
                v = psum(l1, row)
                v2 = v.copy()
                v2 = list(map(str, v2))
                n = rows
                k = "  ".join(v2)
                f = "{p:^90}".format(p=k)
                print(f)
                row = row + 1
                l1 = v
    ptriangle(row)
#Repeating same procedure for different row>16 (The only difference will be in string formatting)
elif row>16 and row<=20:
    def psum(list1, row):
        i1 = 0
        i2 = 1
        l = []
        for i1 in range(row - 1):
            l.append(list1[i1] + list1[i2])
            i1 = i1 + 1
            i2 = i2 + 1
        l.insert(0, 1)
        l.append(1)
        return (l)


    def ptriangle(rows):
        if rows == 1:
            print(1)
        elif rows == 2:
            print(f" 1\n1 1")
        else:
            f = "{p:^120}".format(p=1)
            print(f)
            f = "{p:^120}".format(p="1  1")
            print(f)
            l1 = [1, 1]
            row = 2
            for i in range(rows - 2):
                v = psum(l1, row)
                v2 = v.copy()
                v2 = list(map(str, v2))
                n = rows
                k = "  ".join(v2)
                f = "{p:^120}".format(p=k)
                print(f)
                row = row + 1
                l1 = v
    ptriangle(row)
#Repeating same procedure for different row>20 (The only difference will be in string formatting)
elif row>20 and row<=30:
    def psum(list1, row):
        i1 = 0
        i2 = 1
        l = []
        for i1 in range(row - 1):
            l.append(list1[i1] + list1[i2])
            i1 = i1 + 1
            i2 = i2 + 1
        l.insert(0, 1)
        l.append(1)
        return (l)


    def ptriangle(rows):
        if rows == 1:
            print(1)
        elif rows == 2:
            print(f" 1\n1 1")
        else:
            f = "{p:^240}".format(p=1)
            print(f)
            f = "{p:^240}".format(p="1  1")
            print(f)
            l1 = [1, 1]
            row = 2
            for i in range(rows - 2):
                v = psum(l1, row)
                v2 = v.copy()
                v2 = list(map(str, v2))
                n = rows
                k = "  ".join(v2)
                f = "{p:^240}".format(p=k)
                print(f)
                row = row + 1
                l1 = v
    ptriangle(row)
#Repeating same procedure for large row value (The only difference will be in string formatting)
else:
    def psum(list1, row):
        i1 = 0
        i2 = 1
        l = []
        for i1 in range(row - 1):
            l.append(list1[i1] + list1[i2])
            i1 = i1 + 1
            i2 = i2 + 1
        l.insert(0, 1)
        l.append(1)
        return (l)


    def ptriangle(rows):
        if rows == 1:
            print(1)
        elif rows == 2:
            print(f" 1\n1 1")
        else:
            f = "{p:^700}".format(p=1)
            print(f)
            f = "{p:^700}".format(p="1  1")
            print(f)
            l1 = [1, 1]
            row = 2
            for i in range(rows - 2):
                v = psum(l1, row)
                v2 = v.copy()
                v2 = list(map(str, v2))
                n = rows
                k = "  ".join(v2)
                f = "{p:^700}".format(p=k)
                print(f)
                row = row + 1
                l1 = v
    ptriangle(row)


#Question 3........................................................................

print("Question 3\n")
a=int(input("Enter the first integer: "))
b=int(input("Enter the second integer: "))
c=a%b
d=a//b
print("Remainder is: ", c)
print("Quotient is: ",d)
if(c!=0):
    if (d!=0):
        print("Both values are non zero")
    else:
        print("One value is zero")
else:
    if (d!=0):
        print("One value is zero")
    else:
        print("Both values are zero")
set1=set()
for i in range (4,7):
    f=c+i
    g=d+i
    if(f>4):
        set1.add(f)
        print(set1)
    if(g>4):
        set1.add(g)
        print(set1)

print(set1)
set2=frozenset(set1)
print("Immutable set: ", frozenset(set1))
print("Largest value in the set: ", max(set2))
k=max(set2)
print("Hash value: ", hash(k))
print("")

#Question 4.....................................................................

print("QUESTION 4\n")
class Student:
    def __init__(self, student, sid):
        self.name = student
        self.sid = sid
    
    def __del__(self):
        print("Object destroyed")

#creating object
student1 = Student("Anjali", 21105113)
print("Object created")

#printing the assigned values
print(f"The name of the student is {student1.name} and SID is {student1.sid}.")

#deleting object
del student1
print("")

#Question 5.....................................................................

print("QUESTION_5\n")
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def __del__(self):
        print(f"Employee {self.name} record deleted")

#creating employee records
employee1 = Employee("Mehak", 40000)
employee2 = Employee("Ashok", 50000)
employee3 = Employee("Viren", 60000)

#part a, updating salary
employee1.salary = 70000
print(f"a. The updated salary of the employee {employee1.name} is {employee1.salary}")

#part b, deleting a record
print("b. ", end='')
del employee3

print(" ")


#Question 6.....................................................................

print("QUESTION_6")
#Taking input of a word from the first friend
word = input("Enter the first word: ")

#taking input of a meaningful word with the exact same letters
testword = input("\nEnter a new meaningful word to test your friendship: ")

#defining dictionary from last assignment
def count_in_dict(word):
    count = {}
    list1 = list(word)
    
    n = len(list1)
    for i in range(n):
        if list1[i] in count:
            count[list1[i]] += 1
        else:
            count[list1[i]] = 1
    return count

#test to verify the letters of the new word
if count_in_dict(word) != count_in_dict(testword):
    print("The letters aren't exact, friendship is fake!!")

#shopkeeper's input to verify the word's meaning
def userinput():
    ans = input("\nDoes the word makes sense?(y or n)\n")

    if ans == 'y':
        print("The friends pass the friendship test!\n\n")
    elif ans == 'n':
        print("The word doesn't have a meaning, friendship is fake!\n\n")
    else:
        print("Invalid input!!!!!!!, try again")
        userinput()
userinput()
print("")

