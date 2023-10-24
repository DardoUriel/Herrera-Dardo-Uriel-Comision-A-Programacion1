#12-	Escribir un programa en el que se pregunte al usuario por una frase y una letra,
#y muestre por pantalla el número de veces que aparece la letra en la frase.
prhase = input("ingrese una frase: ")
letter = input("ingrese una letra: ")
cont=0
for i in range(len(prhase)):
    if letter==prhase[i]:
        cont+=1
print(f"esa letra aparecio {cont} veces")