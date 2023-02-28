class Persona:
    #pass
    #Metodo que da valor inicial a los atributos de la clase
    def __init__(self,nombre, edad):
        self.nombre = nombre
        self.edad = edad
    

#Modificar los valores
#Persona.nombre = "Juan"
#Persona.edad = 28

#Acceder a los valores
#rint(Persona.nombre)
#print(Persona.edad)

#Creacion de un objeto
persona = Persona("Karla", 30)
print(persona.nombre)
print(persona.edad)
#para saber direccion de memoria
print(id(persona))

#Creacion de un segundo objeto
persona2 = Persona("Carlos",40)
print(persona2.nombre)
print(persona2.edad)

#para saber direccion de memoria
print(id(persona2))