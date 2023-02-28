class MiClase:

    variable_clase = "Variable clase"
    
    def __init__(self):
        self.variable_instancia = "Variable Instancia"
    
    @staticmethod
    def metodo_estatico():
        print("Metodo estatico")
        print(MiClase.variable_clase)
        #Desde un metodo estatico no podemos acceder a una variable de instancia
        #print(MiClase.variable_instancia)
        
    @classmethod
    def metodo_clase(cls):
        print("Metodo de clase: "+ str(cls))
        print(cls.variable_clase)
        #Desde un metodo clase no podemos acceder a una variable de instancia
        #print(cls.variable_instancia)
        
    def metodo_instancia(self):
        self.metodo_estatico()
        self.metodo_clase()
        print(self.variable_clase)
        print(self.variable_instancia)
            
MiClase.metodo_estatico()
MiClase.metodo_clase()

objeto1 = MiClase()
objeto1.metodo_instancia()