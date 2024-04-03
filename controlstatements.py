"""temp = 40
print(temp <= 50 and temp >= 30)
print(temp < 40 or temp >= 30)
print(nottemp == 40)"""
temp = (float(input ("enter the temperature")))
if temp >= 40:
    print ("its too hot today")
    print( "take enough fluids")
elif temp <= 30:
    print ("its awesome")
elif temp <= 20:
    print("its cool") 
else:
    print("enjoy whatever it is")