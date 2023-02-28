class Persona:
    # __secuencia_persona = 0
    
    def __init__(self,id_persona = None,nombre = None, apellido = None, email= None):
        # Persona.__secuencia_persona += 1
        self.__id_persona = id_persona
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        
    def getId(self):
        return self.__id_persona
        
    def setNombre(self,nombre):
        self.__nombre = nombre
    
    def getNombre(self):
        return self.__nombre
    
    def setApellido(self, apellido):
        self.__apellido = apellido
    
    def getApellido(self):
        return self.__apellido
    
    def setEmail(self, email):
        self.__email = email
        
    def getEmail(self):
        return self.__email
    
    def __str__(self):
        return (f'Id: {self.getId()}, '
                f'Nombre: {self.getNombre()}, '
                f'Apellido: {self.getApellido()}, '
                 f'Email: {self.getEmail()}'
                 )
        
