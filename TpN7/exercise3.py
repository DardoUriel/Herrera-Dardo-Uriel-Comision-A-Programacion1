#Crea una lista de diccionarios, donde cada diccionario contiene
# información sobre un libro (título, autor, año de publicación, etc.). Luego, escribe un programa
# que ordene la lista de libros en función de un campo específico, como el año de publicación o el autor.

# Crear una lista de diccionarios con información sobre libros
import sys
sys.path.append("C:/Users/FlowUser/Desktop/UTN/ProgrmacionRepositorio/Herrera-Dardo-Uriel-Comision-A-Programacion1/Funciones")
from functions import order_books

libros = [
    {
        'titulo': 'El Gran Gatsby',
        'autor': 'F. Scott Fitzgerald',
        'anio_publicacion': 1925
    },
    {
        'titulo': 'Matar a un ruiseñor',
        'autor': 'Harper Lee',
        'anio_publicacion': 1960
    },
    {
        'titulo': '1984',
        'autor': 'George Orwell',
        'anio_publicacion': 1949
    },
    {
        'titulo': 'Cien años de soledad',
        'autor': 'Gabriel García Márquez',
        'anio_publicacion': 1967
    }
]

# Ordenar la lista de libros por año de publicación
libros_ordenados_por_anio = order_books(libros, 'anio_publicacion')
print("Libros ordenados por año de publicación:")
for libro in libros_ordenados_por_anio:
    print(f"Título: {libro['titulo']}, Autor: {libro['autor']}, Año de Publicación: {libro['anio_publicacion']}")

# Ordenar la lista de libros por autor
libros_ordenados_por_autor = order_books(libros, 'autor')
print("\nLibros ordenados por autor:")
for libro in libros_ordenados_por_autor:
    print(f"Título: {libro['titulo']}, Autor: {libro['autor']}, Año de Publicación: {libro['anio_publicacion']}")
