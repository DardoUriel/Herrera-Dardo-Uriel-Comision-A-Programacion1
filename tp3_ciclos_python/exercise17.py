#17-	Solicitar al usuario que ingrese una frase y 
#luego imprimir un listado de las vocales que aparecen en esa frase (sin repetirlas).
phrase = input("ingrese una frase: ")
cont_a=0
cont_e=0
cont_i=0
cont_o=0
cont_u=0
for i in range(len(phrase)):
    if phrase[i].lower() =="a" and cont_a==0:
        print(phrase[i])
        cont_a+=1
    elif phrase[i].lower() =="e" and cont_e==0:
        print(phrase[i])
        cont_e+=1
    elif phrase[i].lower() =="i" and cont_i==0:
        print(phrase[i])
        cont_i+=1
    elif phrase[i].lower() =="o" and cont_o==0:
        print(phrase[i])
        cont_o+=1
    elif phrase[i].lower() =="u" and cont_u==0:
        print(phrase[i])
        cont_u+=1


