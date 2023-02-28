try:
    archivo = open("prueba.txt","w")
    archivo.write("Agregamos info al archivo\n")
    archivo.write("Adios")
except Exception as e:
    print(e)
finally:
    archivo.close()
    #despues de close ya no podemos trabajar con el archivo
    
    #archivo.write("Saludos")
    
