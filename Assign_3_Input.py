#QUESTION_1
print("QUESTION_1")
string_name=str(input("Enter the string:"))
#Taking each string as element in list
list1=string_name.split()
#empty list which will contain lowercase words only
list_l=[]
#converting each element of list1 to lowercase and inserting it to list_l
for e in list1:
    lower_e=e.lower()
    list_l.append(lower_e)
#converting list_l to set to avoid repeatation
set1=set(list_l)
dic={}
#forming a dictionary with key string and value string count
for el in set1:
    count=list_l.count(el)
    dic.update({el:count})
#Code when string contains only one word
dic2={}       #empty dictionary
set2={1,2}
set2.clear()  #empty set2
list2=[]      #empty list2
#Condition when only one word is detected in string
if len(list1)==1:
    #Code for counting letter
    #Adding all letters of input string into  list2
    for elements in string_name:
        list2.append(elements)
    #lowering elements of list2 to lowercase and adding to set2
    for el in list2:
        set2.add(el.lower())
    #lowering main input string to lowercase
    string_l=string_name.lower()
    for elem in set2:
        #Adding count values to dic2
        dic2.update({elem:string_l.count(elem)})
    # printing the dic2 containing 'letter':'letter count'
    print("\nDictionary containing 'Letter':'Letter Count' is shown below:")
    print(dic2)
#printing the dic when string contains more than one word
else:
    print("\nDictionary containing {'Word':'Word Count'} is:")
    print(dic)      #dic contains 'word':'word count'


#QUESTION_2
print("QUESTION_2")
#Defining leap year function
def leapyear(x):
    #for leap year this condition must be True
    if (x%400)==0 or ((x%100!=0) and (x%4==0)):
        return True
    else:
        return False
#Taking input day,month,year
day=int(input("Enter Day in range[1-31]:"))
month=int(input("Enter Month in range[1-12]:"))
year=int(input("Enter Year in range[1800-2025]:"))
#Applying condition1 for dates out of range
if day<1 or day>31 or month<1 or month>12 or year<1800 or year>2025:
    condition1=False
else:
    condition1=True

#Applying condition2 when day entered does not present in that month
month_31 = [1, 3, 5, 7, 9, 11]  #List containing month with 31 days
month_30 = [4, 6, 8, 10, 12]    #List containing month with 30 days
#for day entered 31 does not present in that month
c1a= day==31 and (month in month_30)
#for day entered greater than 29 in month february i.e 2
c1b= day>29  and month==2
#for day entered greater than 28 in february in non leapyear
c1c= day==29 and (not leapyear(year)) and month==2
if c1a or c1b or c1c :
    condition2=False
else:
    condition2=True
#printing error when date entered is not correct
if c1a:
    print(f"\nError!!\n{day} Sorry day can't be in month {month}")
elif c1b:
    print(f"\nError!!\n{day} Sorry day can't be in month {month}")
elif c1c:
    print(f"\nError!!\n{day} Sorry day can't be in month {month} as the year {year} in not leapyear")
elif condition1==False:
    print(f"\nError!!\nPlease enter date in range day[1-31], month[1-12], year[1800-2025] ")

#Code when date entered is correct
if condition1==True and condition2==True :
    month_31 = [1, 3, 5, 7, 9, 11]  #List containing month with 31 days
    month_30 = [4, 6, 8, 10, 12]    #List containing month with 30 days
    #For month with 31 days
    if (month in month_31) == True:
        if day == 31:
            day = 1
            month = month + 1
        elif 1 <= day <= 30:
            day = day + 1
    #For month with 30 days
    elif (month in month_30) == True:
        if day == 30 and month == 12:
            day = 1
            month = 1
            year = year + 1
        elif day == 30 and month != 12:
            day = 1
            month = month + 1
        elif 1 <= day <= 29:
            day = day + 1
    #for february month i.e. month 2
    elif month == 2:
        # If year is leap year
        if leapyear(year) == True:
            if day == 29:
                day = 1
                month = month + 1
            elif 1 <= day <= 28:
                day = day + 1
        # If year is not leap year
        elif leapyear(year) == False:
            if day == 28:
                day = 1
                month = month + 1
            elif 1 <= day <= 27:
                day = day + 1
    # Printing Next date
    print(f"\nNext Date in format Day/Month/Year is: {day}/{month}/{year}")


#QUESTION_3
print("QUESTION_3")
#Taking input list
list1=list(map(int,input("Enter the numbers separated by space:").split()))
#creating an Empty list
newList=[]
#Forming square and storing in tuple
for e in list1:
    t=(e,e*e)
    newList.append(t)
#Printing the final result
print("\nList containing (n,n^2): ",(newList))


#QUESTION_4
print("QUESTION_4")
#Taking grade point input
grade_points=int(input("Enter your grade points:"))
#Forming a dictionary of statements
dic={10:"Your grade is 'A+' and Outstanding performance.",
     9:"Your grade is 'A' and Excellent performance.",
     8:"Your grade is 'B+' and Very Good performance.",
     7:"Your grade is 'B' and Good performance.",
     6:"Your grade is 'C+' and Average performance.",
     5:"Your grade is 'C' and Below Average performance.",
     4:"Your grade is 'D' and Poor performance."}
#Applying Conditions for correct grade range
if 4<=grade_points<=10:
    #Taking required statement from dictionary
    statement=dic.get(grade_points)
    #printing final result
    print(statement)
else:
    #printing error message when grade is out of range
    print("\nError!!\nPlease enter grade only in range [4,10]")


#QUESTION_5
print("QUESTION_5")
alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']

for row in range(0,6):
    column=0
    counter=0
    while column<11:
        if column<row or column>11-row-1:
            print(" ", end="")

        else:
            print(alphabets[counter], end="")
            counter=counter+1
        column=column+1
    print("")
    


#QUESTION_6
print("QUESTION_6")
condition=True

#Defining dictionary to store the values
Dictionary={}
prompt="y"
while condition:
    if prompt.lower()=="y":
        SID=int(input("Please Enter SID of Student- "))
        name=input("Please enter the name of the Student- ")
        Dictionary[SID]=name
        prompt= input("If you want to enter more details press Y/N- ")
        condition = True

    else:
        condition = False

print("Part a")
for key,value in Dictionary.items():
    print(f"{key} is {value}")
print("")

print("Part b")
Values_sort_dict= sorted(Dictionary.values())
print(f"value sorted dictionary is {Values_sort_dict}")
print("")

print("Part c")
Key_sort_dict= sorted(Dictionary.keys())
print(f"Keys sorted dictionary is {Key_sort_dict}")
print("")

print("Part d")
SID_required=int(input("Please enter the student's SID whose detail you need- "))
if SID_required in Dictionary.keys():
    print(f"Name of the required student is {Dictionary[SID_required]}")
else:
    print("The SID is not present in the given Data")


#QUESTION_7
print("QUESTION_7")
#Taking input
n=int(input("Enter number of elements N in fibonacci series:\n[N must be positive Integer]: N="))
#printing error message when N<=0
if n<=0 :
    print("\nError\nNumber of elements in fibonacci series must be integer and greater than zero.")
#code for fibonacci series
else:
    #code for fibonacci series for first 2 elements
    if n == 1:
        print("\nThe fibonacci series with 1 element is shown below\n[1]")
        print("\nAverage of given fibonacci series is", 1)

    elif n == 2:
        print("\nThe fibonacci series with 2 element is shown below\n[1,1]")
        print("\nAverage of given fibonacci series is", 1)
    #General code for fibonacci for next N-2 elements
    else:
        # List of fibonacci elements with 1,1 as initial elements
        list1 = [1, 1]
        #Building logic to get fibonacci series
        a = 1
        b = 1
        # For loop
        for i in range(n - 2):
            s = a + b
            list1.append(s)
            a = b
            b = s
        # printing the final fibonacci series
        print(f"\nThe fibonacci series with {n} elements is shown below:")
        print(list1)
        # Finding average of fibonacci series
        sum = 0    #intial sum=0
        # finding sum of all elements in list1
        for num in list1:
            sum = sum + num
        average = (sum / n)
        # Till two decimal place
        two_decimal = "{:.2f}".format(average)
        # printing average
        print(f"\nAverage of given fibonacci series is {two_decimal}")



#QUESTION_8
print("QUESTION_8")
print(" ")
Set1= {1, 2, 3, 4, 5}
Set2= {2, 4, 6, 8}
Set3= {1, 5, 9, 13, 17}
print("Finding symmetric difference of both the sets")
print("Part a")
set_notboth=Set1^Set2
print(f"set with elements not common in both is {set_notboth}")
print(" ")

print("Finding symmetric difference of all sets")
print("Part b")
set_onlyinone=Set1^Set2^Set3
print(f"Set of elements that is only present in one set is {set_onlyinone}")
print(" ")

print("Finding elements that is common in any two sets")
print("Part C")
set_onlyintwo=(Set1|Set2|Set3)- (Set1^Set2^Set3)-(Set1&Set2&Set3)
print(f"Set of elements that is only present in two set is {set_onlyintwo}")
print(" ")

print("Finding elements common in set1 and range 1 to 10")
print("Part d")
new_set1=set()
for n in range(1,11):
    new_set1.add(n)
not_common_1=new_set1- Set1
print(f"set of all integers in the range 1 to 10 that are not in Set1 {not_common_1}")
print(" ")

print("Part e")
print("Finding elements common in sets 1,2,3 and range 1 to 10")
new_set2=set()
for n in range(1,11):
    new_set2.add(n)
not_common_2=new_set2 - (Set1|Set2|Set3)
print(f"set of all integers in the range 1 to 10 that are not in Set1 and Set2 and Set3 {not_common_2}")







