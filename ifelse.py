a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number : "))

if(a>b):
    if(a>c):
        print(a,"is the greatest")

    else:
        print(c,"is the greatest")

elif(b>c):
    print(b,"is the greatest")

else:
    print("all numbers are equal")
      


