# printing length
a = "talal"
b = "iqbal"

print(len(a))
print(len(b))

# length count including wide space
c = "talal" + " "+ "iqbal"
print(len(c))
                                            
                                            # Conditional Statement

#traffic light program
light =input("enter the light : ")

if(light == "red"):
    print("STOP")

elif(light == "yellow"):
    print("START")

else:
    print("GO")

#Students grades on basis of marks
marks = int(input("enter your marks : "))

if(marks >= 90 and marks <= 100):
    print("grade A")
elif(marks >=80 and marks < 90):
    print(" Grade B")
elif( marks >= 70 and marks < 80):
    print("Grade c")
elif( marks >= 60 and marks < 70):
    print("Grade D")
else:
    print(" you are failed re atempt ")
print("the programs end ... THANKYOU")

#find the greatest of all
a = int(input("enter the first number : "))
b = int(input("enter the second number : "))
c = int(input("enter the third number : "))

if(a > b and a > c):
    print(" a is greatest of all")
elif(b>a and b>c):
    print(" b is greatest of all")
else:
    print(" c is greatest of all")