num=int(input("enter a number :"))
file = open("result.text","w")
if num%2==0:
    file.write("even")
else:
    file.write("odd")
    file.close()
