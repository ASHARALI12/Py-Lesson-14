def divide(num1,num2):
    return num1 / num2
def multiply(num1,num2):
    return num1 * num2
def subtract(num1,num2):
    return num1 - num2
def add(num1,num2):
    return num1 + num2
x = (input("What You Will Like To Do,Division,Subtraction,Addition,Multiplication? "))
y = int(input("Enter One Number: "))
z = int(input("Enter Another Number: "))
if x == "Division":
    print("The Division Of Above Numbers Given are: ",divide(y,z))
elif x == "Subtraction":
    print("The Subtraction Of Above Numbers Given are: ",subtract(y,z))
elif x == "Multiplication":
    print("The Multiplication Of Above Numbers Given are: ",multiply(y,z))
elif x == "Addition":
    print("The Addition Of Above Numbers Given are: ",add(y,z))

