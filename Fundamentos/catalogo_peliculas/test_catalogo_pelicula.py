from dominio.pelicula import Pelicula
from servicio.catalogo_peliculas import CatalogoPelicula

opcion = None
while opcion != "4":
    print("Opciones:")
    print("1. Agregar pelicula:")
    print("2. Listar peliculas")
    print("3. Eliminar catalogo de peliculas")
    print("4. Salir")
    opcion = input("Escribe tu opcion (1-4):")
    
    if opcion == "1":
        nombre_pelicula = input("Proporciona el nombre de la pelicula: ")
        pelicula = Pelicula(nombre_pelicula)
        CatalogoPelicula.agregar_pelicula(pelicula)
    elif opcion == "2":
        CatalogoPelicula.listar_peliculas()
    elif opcion == "3":
        CatalogoPelicula.eliminar()
else:
    print("Salimos del programa...")