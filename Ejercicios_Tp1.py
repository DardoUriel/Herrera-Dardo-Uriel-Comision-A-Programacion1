#⦁	Declara una variable de cada tipo de dato y asígnale un valor.
#int
var1 = 10
#float
var2 = 7/2
#complex
var3 = 7j
#str
var4 = "hola"
#bool
var5 = True
#lista
mi_lista = [1,2,3,4,5]
#tupla
mi_tupla= (1,2,3,4,5)
#dic
mi_diccionario ={
    "nombre" : "Uriel",
    "edad" : 19,
    "ciudad":"Mendoza"

}
#null
var6 = None

#⦁	Métodos upper(), lower() y title(). 
#⦁	Pon en mayúsculas la primera letra de cada palabra del siguiente nombre: ‘lucas mauricio barros’.
nombre = 'lucas mauricio barros'
print(nombre.title())
#⦁	Deja esta frase totalmente en letras minúsculas: ‘El qUe No arRiesGa, nO gANa.’
minusculas ='El qUe No arRiesGa, nO gANa.'
print(minusculas.lower())
#⦁	Deja esta frase totalmente en letras mayúsculas: ‘El qUe No arRiesGa, nO gANa.’
mayusculas ='El qUe No arRiesGa, nO gANa.'
print(mayusculas.upper())
#⦁	Convierte en expresiones algorítmicas las siguientes expresiones algebraicas.
#  Coloca paréntesis solamente donde sean necesarios
#a)
a = 1
b = 1
c = 1
resultado_a = (b/2)-(4*a*c)
#b) 
x=1
y=1
resultado_b = (3*x*y) - (5*x)+(12*x)-17
#c)
d=1
resultado_c =(b+d)/(c+4)
#d)
resultado_d = ((x*y)/y)+2
#e)
z=1
resultado_e = (1/y)+((3*x)/z)+1  
#f)
resultado_f = (1/(y+3))+(x/y)+1    
# g)
resultado_g =a**2+b**2    
# h)
resultado_h =(a+b)**2
# i)
resultado_i = b** (1/3) + 34
# j)
import math
w=1
resultado_j = x/y * (z + w) * math.pi
# k)
u=1
resultado_k = (x + y) / (u + w/b)
#⦁	Crea una lista que contenga los siguientes valores en las posiciones indicadas
# 'uno' en la posición 4
# 'dos' en la posición 1
# 'tres' en la posición 0
# 'cuatro' en la posición 3
# 'cinco' en la posición 2
la_lista = ['tres','dos','cinco','cuatro','uno']
#⦁	Imprime la segunda posición de esta tupla.
colores = ('rojo','azul','verde','amarillo','marrón','lila','negro','rosa','blanco','naranja')
print(colores[2])
#⦁	Utiliza los símbolos de suma y resta para obtener el resultado 25 
# a partir de los elementos de la siguiente tupla en una variable llamada operacion
numeros = (10,1,5,11)
operacion = ((numeros[0]+numeros[3])-numeros[1])+numeros[2]
print(operacion)
#⦁	Solicita dos números al usuario, súmalos e imprime el resultado
numero1 = int(input("Escriba un numero: "))
numero2 = int(input("Escriba otro numero: "))
print("el resultado de la suma es: ", (numero1 + numero2) )
#⦁	Solicita la edad de una persona, calcula cuántos años faltan para que cumpla 100 años e imprime el resultado.
edad = int(input("ingresar edad: "))
print(f"Te faltan {100 - edad} años para cumplir 100 años") if edad < 100 and edad > 0 else print("la edad ingresada no es valida")
#⦁	Comprobar si un número es par o impar.
num = int(input("numero entero: "))
print("el numero es par") if num % 2 == 0 else print("el nuemro es impar")

#	Obtener el valor absoluto de un número.
num = int(input("ingrese un numero: "))
print(f"El valor absoluto de {num} es: {num * -1}") if num < 0 else print("El numero ya está en su valor absoluto")

#	Comparar dos números y obtener el mayor.
num1 = int(input("numero 1: "))
num2 = int(input("numero 2: "))
son_iguales = num1 == num2
print(f"El mayor es: {num1}") if num2 < num1 else print(f"El mayor es: {num2}") 

