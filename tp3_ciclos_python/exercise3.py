number = -5
while (number <= 0):
    number=int(input("ingrese un numero "))
for i in range(number+1):
    if (i)%2!=0:
        if i==number or i==number-1:
            print(i , end = "")
        else:
            print(i , end = "-")
    
    