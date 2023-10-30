'''
⦁Crea una función que reciba como parámetro un texto y devuelve una cadena con un espacio 
adicional tras cada letra. Por ejemplo, “Hola, tú” devolverá “H o l a , t ú “. 
Crea un programa principal donde se use dicha función.
'''

import sys
sys.path.append("C:/Users/FlowUser/Desktop/UTN/ProgrmacionRepositorio/Herrera-Dardo-Uriel-Comision-A-Programacion1/Funciones")
from functions import letter_spacing 

sentence ="Hola, tú"
print(letter_spacing(sentence))
