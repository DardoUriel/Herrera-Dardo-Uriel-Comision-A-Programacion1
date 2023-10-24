#15-	Escriba un programa que pida un número entero mayor que cero y que escriba sus divisores.
num=0
while num<=0:
    num=int(input("ingrese un numero: "))
for i in range(1,num+1):
    if num%i==0:
        print(i,end=" ")