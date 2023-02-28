class Persona:
    #Metodo constructor
    def __init__(self, n):
        self.__nombre = n
        self.__edad = 18

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, n):
        self.__nombre = n


    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        self.__edad = edad


p1 = Persona("Karla")
#print(p1.__nombre) marca un error
print(p1.get_nombre())
print(p1.get_edad())

#p1.__nombre = "Juan"
p1.set_nombre("Juan")
print(p1.get_nombre())
p1.set_edad(20)
print(p1.get_edad())
