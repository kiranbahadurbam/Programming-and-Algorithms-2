#Adding two number 

def add(a,  b):
    sum = a + b
    print(a, "+", b, "=", sum)

#Subtraction of two number

    def subtract(a, b):
        difference = a - b 
        print(a, "-", b, "=",difference)

#multiplication of two number
 
    def multiply(a, b):
        product = a * b 
        print(a, "x", b, "=", product)

#division of two number

    def divide(a, b):
        division = a / b 
        print(a, "/", b, "=", division)


print("Welcome to calculator\n")

while True:
    print("Menu")
    print("1. Addition of two number")
    print("2. Addition of two number")
    print("3. Addition of two number")
    print("4. Addition of two number")
    print("5. Exit")
    user_choice = int(input("\nEnter your choice: "))

    if user_choice == 1:
        print("performing Addition\n")
        a = int( input("Enter First Number: "))  
        b = int( input("Enter Second Number: "))  
        add(a, b) 

    elif user_choice == 2:
        print("Performing Subtraction\n")
        a = int( input("Enter First Number: "))  
        b = int( input("Enter Second Number: "))
        subtract(a, b)

    elif user_choice == 3:
        print("Performing Multiplication\n")
        a = int( input("Enter First Number: "))  
        b = int( input("Enter Second Number: "))
        multiply(a, b)

    elif user_choice == 4:
        print("Performing Division\n")
        a = int( input("Enter First Number: "))  
        b = int( input("Enter Second Number: "))
        divide(a, b)

    elif user_choice == 5:
        break

    else:
        print("please enter the valid input from the list")


    
#pyinstaller --onefile .\menu_driven.py
#pip install pyinstaller