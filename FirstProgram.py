# #type check
x = 5
y = 2.5
z = "python"

print(type(x))
print(type(y))
print(type(z))

#user input
username = input("enter your name : ")
print("Hello world",username)

# #sum of two numbers
firstnum = int(input("enter the first number : "))
secnum = int(input("enter the second number : "))
sum =(firstnum + secnum)

print("the sum of two numbers is : ", sum)

# # square of given number
number = int(input("enter the number for square : "))
print("the square of the given numb is : ",number**2)

# # type conversion
a = 12.334
a = int(a)
print(a)
print(type(a))

# # arthimetic operations
a = 10
b = 4

print("sum of a and b is : ",a+b)
print("diff of a and b is : ",a-b)
print("multi of a and b is : ",a*b)
print("div of a and b is : ",a/b)
print("reminder of a and b is : ",a%b)


# # Area calculation
length =int( input('enter the length of rectangle : '))
width = int(input("enter the widht of retangle : "))

area = length * width
print("the area of rectangle is : ", area)

#Percetage calculations
math = int(input("maths : "))
urdu = int(input("urdu : "))
english = int(input("english : "))
phy = int(input("phy : "))
comp = int(input("comp : "))

total_marks = 500
gain_marks = (math + urdu + english + phy +comp)
percentage = (gain_marks/total_marks) * 100

print("percentage is : ",percentage)

# #number swaps
a = 10
b = 20

a , b = b , a 
print(a)
print(b)

# # F string
first_name = "talal"
last_name = "iqbal"

print(f"my first name is : {first_name } and last name is : { last_name}")





