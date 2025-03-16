print("Hello there lets see how many more years u got until u reach 120")
try:
    age = int(input("Enter your age please: ")) 
except ValueError:
    print("Age ought to be a number u knucklehead")
    exit()    

result = 120 - age  

if age >= 120:
    print("Not you, you're old as f***! u shady cunt")  
    print("thank U")
elif age <=20:
    print(f"Oh look at u, u lil {age} years old rascal, u got {result} years to go.")
    print("thank U")
elif age >= 100:
    print(f"hang in there ur just {result} years away from 120")
    print("thank U")
else:
    print(f"You are {result} years away from 120.")  
    print("thank U")

