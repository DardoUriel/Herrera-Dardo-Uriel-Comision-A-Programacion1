"""5.	¿Qué problemas tienen las siguientes instrucciones?¿Cómo las solucionarías?"""
#a)	A = input(nombre, “¿Cuál es tu canción favorita?”) la coma no sirve para unir variable con string en el input, el nombre de la variable no representa de ninguna manera el contenido de esta, y no hay separación entre la pregunta, el nombre y el espacio a escribir
name = "Gabriel"
favorite_song = input(name + ", ¿Cuál es tu canción favorita? ") #solucionado
#b)	precio = input(“Precio: “) el input devuelve string, el cual no se puede usar para calculos, se debe poner adentro de la función float()
# total = precio + (precio * 0.1)
price = float(input("Precio: "))#solucionado
total = price + (price * 0.1)
#c)	edad = int(input(“Edad: “)) 
#print(tu edad es, edad) faltaron comillas
age = int(input("Edad: "))
print("Tu edad es: ", age)#solucionado
#d)	edad = int(input(“Edad: “))
#print(“Veamos si tu edad es 18…”, edad=18) esa comprobación se debe hacer con la función if, no sirve ni funciona ponerla adentro del print
age2 = int(input("Edad: "))
if age2 == 18:
    print("Tenés 18")
else:
    print("No tenés 18")#solucionado


