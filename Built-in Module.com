import math 
n=int(input("enter a number :"))
print("even"if math.fmod(n,2)==0 else "odd")
