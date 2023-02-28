#set es una coleccion sin orden y sin indices, no permite elementos repetidos
#y los elementos no se pueden modificar, pero si agregar nuevos o eliminar
planetas = {"Marte", "Jupiter","Venus"}
print(planetas)
#print(type(planetas))
#largo
print(len(planetas))
#revisar si un elemento esta presente
print("Marte" in planetas)
#agregar 
planetas.add("Tierra")#no se pueden agregar elementos duplicados
print(planetas)
#eliminar con remove posiblemente arroja excepcion
planetas.remove("Tierra")
print(planetas)
#eliminar con discard no arroja excepcion
planetas.discard("Jupiters")
print(planetas)
#limpiar el set
planetas.clear()
print(planetas)
#eliminar el set
del planetas
