num=int(input("enter the number :"))
sum = 0
n = num
while(n>0):
    r = n%10
    sum += r**3
    n //= 10
if(num==sum):
    print("number is armstrong")
else:
    print("number is not armstrong")