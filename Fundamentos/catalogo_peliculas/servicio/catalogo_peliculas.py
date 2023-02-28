import os
class CatalogoPelicula:
    
    ruta_archivo = "peliculas.txt"
    
    @staticmethod
    def agregar_pelicula(pelicula):
        try:
            #"a" modo append
            archivo = open(CatalogoPelicula.ruta_archivo, "a")
            archivo.write(pelicula.__str__()+"\n")
        except Exception as e:
            print("Ocurrio una excepcion al agregar: ",e)
        finally:
            archivo.close()
            
    @staticmethod
    def listar_peliculas():
        try:
            archivo = open(CatalogoPelicula.ruta_archivo, "r")
            print("Catalogo de Peliculas")
            print(archivo.read())
        except Exception as e:
            print("Ocurrio un error al listar pelicula: ",e)
            
        finally:
            archivo.close()
            
    @staticmethod
    def eliminar():
        try:
            os.remove(CatalogoPelicula.ruta_archivo)
            print("archivo eliminado",CatalogoPelicula.ruta_archivo)
        except Exception as e:
            print("Ocurrio un error al eliminar",e)
