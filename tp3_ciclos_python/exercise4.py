number = -1
lista = []
while number<=0:
    number = int(input("ingrese un numero positivo "))
while number>-1:
    if number==0:
        print(number , end = "")
    else:
        print(number , end = ",")
    number-=1 