#19-	Escriba un programa que simule una alcancía. 
#El programa solicitará primero una cantidad, que será la cantidad de dinero que queremos ahorrar. 
#A continuación, el programa solicitará una y otra vez las cantidades que se irán ahorrando, 
#hasta que el total ahorrado iguale o supere al objetivo. 
#el programa deberá comprobar que las cantidades ingresadas sean positivas.
amout = int(input("ingrese una cantidad que quiere ahorrar: "))
total=0
while True:
    enter_savings = int(input("ingrese la cantidad que quiere aportar para ahorrar: "))
    total+=enter_savings
    if total>=amout:
        break
print(total)