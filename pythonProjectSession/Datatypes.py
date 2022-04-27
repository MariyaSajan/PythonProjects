#int
#float
#str
#bool
#list
#dict
#tup
#set

x=10
y=20
sum = x+y
print("The sum of x and y is", sum)

c=1.2
d=20.3
sum1= c+d

print("The sum of c and d is", sum1)

name="pam"
desg="tester"

is_valid_user = True

#use snakecasing in python(by using underscore)
#variables cant have white space
#cant use special character
#good to use small letter
#avoid using built in keywords
#variable names are case sensitive

area = 10
print(type(area))

area = "10"
print(type(area))

#python is a dynamically typed language, whereas  java is a statically typed

#To calculate tax

income = 10000
tax_percentage = 0.2

tax= income * tax_percentage
print(tax)

#Strings - ordered sequence of characters


name ="Maria"
first_name = 'riya'

#Indexing and slicing

print(name[0])


#Printing the length of a string
print(len(name))
print(len(first_name))

#slicing

str_alphabets = "abcdefg"
print(str_alphabets[0:4])
print(str_alphabets[2:])
print(str_alphabets[0:7:2])

#string is immutable

t= "Example"
print type(t)
t[0] = "M"
#This cannot be done as strings are immutable
