number = int(input("Enter a number : "))
print("number is : ", number)
if number%2==0:
    print("number is even")
else:
    print("number is odd")


weight = int(input("Enter your weight in kg : "))
height = int(input("Enter your weight in cm : "))
BMI = weight/(height/100)**2
print("your BMI is : ", BMI)

if BMI<18.5:
    print("You are underweight")
elif BMI>=18.5 and BMI<24.9:
    print("You are normal")
else:
    print("You are obese")

import datetime
current_time = datetime.datetime.now()
print("current time is : ", current_time)

import calendar
print(calendar.month(2025, 10))
print("\n", calendar.calendar(2025))


num= int(input("enter a number : "))
if num > 50:
    if num % 2 == 0:
        print("number is even")
    else:
        print("number is odd")
else : print("number is less than 50")



for i in range(1,11):
    print(f"23 x {i} = {23*1}")
          

n= int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("#", end=" ")
    print( )


total_sum= sum(range(1,21))
print(f"the sum of first ten natural numbers is : {total_sum} ")


num = int(input("Enter a number: "))
if num>1:
    for i in range(2,num):
        if (num%i)==0:
            print(f"{num} is not a prime number")
            break
else:
    print(f"{num} is a prime number")


def intro(name):
    print("Hi, I am " + name + " I am a boy, and I like playing basketball.")


user_name=input("Enter your name")
intro(user_name)



def recr_factorial(n):
    if n==1:
        return n
    else:
        return n* recr_factorial(n-1)
num= int(input("Enter a number: "))
if num<0:
    print("Sorry, factorial does not exist for negative numbers")
    print("Enter a positive number")
elif num==0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of", num, "is", recr_factorial(num))

#acitivty 3
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

num1= int(input("Enter first number: "))
num2= int(input("Enter second number: "))
print("Addition of two numbers is: ", add(num1,num2))
print("Subtraction of two numbers is: ", sub(num1.num2))
print("Multiplication of two numbers is: ", mul(num1,num2))
print("Division of two numbers is: ", div(num1,num2))
print("Thank you for using this calculator")


