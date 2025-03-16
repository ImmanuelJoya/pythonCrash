a = int(input("enter ur 1st number:"))
b = int(input("enter ur 2nd number:"))
c = input("Enter the operaton u wanna use among the given (+, -, *, /)")

def Calculator(a, b, operation):
    if operation == "+":
        res = a + b 
    elif operation == "-":
        res = a-b
    elif operation == "*":
        res = a*b
    elif operation == "/":
        res = a/b if b != 0 else "undefined"
    else: res = "invalid operation"     
    
    print(f"Result:{res}")
    
    # calling the function 
Calculator(a, b, c)