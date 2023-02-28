#archivo = open("//home//junior//Escritorio//Cursos//Python//proyecto_python//prueba.txt","r")
archivo = open("prueba.txt","r")
#print(archivo.read())


#leer algunos caracteres
#print(archivo.read(5))

#leer lineas completas
#print(archivo.readline())
#print(archivo.readline())

#iterando
#for linea in archivo:
#    print(linea)

#leer varias lineas
#print(archivo.readlines())

#acceder a una linea de la lista
#print(archivo.readlines()[1])

#Abrimos un nuevo archivo
#con a anexamos informacion a nuestro archivo
#archivo2 = open("copia.txt", "a")
archivo2 = open("copia.txt", "w")

archivo2.write(archivo.read())
archivo.close()
archivo2.close()
