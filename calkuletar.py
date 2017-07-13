def add(x,y):
    print(x+y)
def sub(x,y):
    print(x-y)
def mult(x,y):
    print(x*y)
def div(x,y):
    print(x/y)


def calculator():
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    op=input("What operation do you want to perform?(+,-,*,/): ")
    print("Ans= ",end='')

    if op=='+':
        add(a,b)
    elif op=='-':
        sub(a,b)
    elif op=='*':
        mult(a,b)
    elif op=='/':
        if b==0:
            print("Error")
        else:
            div(a,b)
    else:
        print("Invalid operator!!")
    again()

def again():
    print("Do you wish to calculate again?")
    c=input("Press 'y' to calculate, 'n' to exit: ")
    if c=='Y':
        calculator()
    elif c=='N':
        print("Thank you")
    else:
        again()

calculator()
        
