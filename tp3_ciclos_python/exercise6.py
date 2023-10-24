number = int(input("ingrese un valor "))
string = "*"
cont=1
j=0
for i in range(number):
    if cont==j:
        cont+=1
        j=0
        print(" ")
    while cont>j :
        print(string , end="")
        j+=1
