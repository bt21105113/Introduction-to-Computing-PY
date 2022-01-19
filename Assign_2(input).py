#   Assignment_2

#QUESTION_1
print("QUESTION_1:")
#[a] (size of string)
string=str(input("Enter the string: "))
print("(a) Size if string is: ", len(string))

#[b] (reverse string)
newString=string[::-1]
print("(b) The reversed string is: ", newString)

#[c] (slicing string)
S=slice(10, 26)
print("(c) New string after slicing: ", string[S])

#[d] (replace substring)
a=string.replace('a case sensitive', 'object oriented')
print("(d) Replacing substring: ", a)
#[e] (finding index of substring)
i=string.index('a')
print("(e) The index of 'a' is: ", i)

#[f] (removing spaces from the string)
r=string.replace(' ','')
print("(f) Removing white spaces: ", r)

#QUESTION_2
print("QUESTION_2:")
Name='Anjali'
SID=21105113
Department='ECE'
CGPA=10
print("Hey, %s Here! \nMy SID is %d \nI am from %s department and my CGPA is %d." % (Name, SID, Department, CGPA))


#QUESTION_3
print("QUESTION_3:")
a=56
b=10
print("a. a & b=%d" % (a & b))
print("b. a | b=%d" % (a | b))
print("c. a ^ b=%d" % (a ^ b))
print("d. Left shift both a and b with 2 bits : a=%d, b=%d" % (a<<2, b<<2))
print("e. Right shift a with 2 bits and b with 4 bits : a=%d, b=%d"%(a>>2, b>>4))

#QUESTION_4
print("QUESTION_4:")
num1=int(input("Enter the 1st number: "))
num2=int(input("Enter the 2nd number: "))
num3=int(input("Enter the 3rd number: "))
if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)
    
#QUESTION_5
print("QUESTION_5:")
string=str(input("Enter the string : "))
if "name" in string:
    print("Yes")
else:
    print("No")

#QUESTION_6
print("QUESTION_6: (Valid or Unvalid triangle sides)")
side_1=int(input("Enter the 1st side of the triangle : "))
side_2=int(input("Enter the 2nd side of the triangle : "))
side_3=int(input("Enter the 3rd side of the triangle : "))
if side_1 < side_2+ side_3 and side_2 < side_1 + side_3 and side_3 < side_2+ side_1:
    print("Yes")
else:
    print("No")    
    


