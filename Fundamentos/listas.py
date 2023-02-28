nombres = ["Juan","Karla","Ricardo","Maria"]
print(nombres)
#conocer el largo de la lista
print(len(nombres))
#elemento 0
print(nombres[0])
print(nombres[1])
#navegacion inversa
print(nombres[-1])
print(nombres[-2])
#imprimir rango
print(nombres[0:2])#sin incluir el indice 2
#imprimir los elementos de inicio hasta el indice proporcionado
print(nombres[0:3])#sin incluir el indice 3
#imprimir los elementos hasta el final desde el indice proporcionado
print(nombres[1:])
#cambiar los elementos de una lista
nombres[3]= "Ivone"
print(nombres)
for nombre in nombres:
    print(nombre)

#revisar si existe un elemento en la lista
if "Carla" in nombres:
    print("Karla si existe en la lista")
else:
    print("el elemento buscado no existe en la lista")
    
#agregar un nuevo elemento
nombres.append("Lorenzo")
print(nombres)
#insertar un nuevo elemento en el indice proporcionado
nombres.insert(1,"Octavio")
print(nombres)
#remover el ultimo elemento de nuestra lista
nombres.pop()
print(nombres)
#remover el indice indicado de la lista
del nombres[0]
print(nombres)
#limpiar los elementos de nuestra lista
nombres.clear()
print(nombres)