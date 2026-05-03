# create a file mymodule.py
def check(n):
    if n%2==0:
        return"even"
    else:
        return"odd"
    # Main file 
    import mymodule 
    n=int(input("enter a number "))
    result=mymodule.check(n)
    print(result)
