a=int(input("enter any number : "))
if(a==0):
    fact  = 1
fact = 1
for i in range(1,a+1):
    fact = fact *i
print("factorial of num ", a, "is", fact)
