class MiClase:
    variable_clase = "Variable de Clase"
    
    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia #variable de instancia
    

print(MiClase.variable_clase)
objeto01 = MiClase("Variable instancia")
MiClase.variable_instancia = "VALOR MODIFICADO"
print(MiClase.variable_instancia)
print(objeto01.variable_instancia)

#Podemos acceder a la variable de clase desde el objeto
print(objeto01.variable_clase)

#Podemos acceder a la variable de clase con el nombre de la clase
print(MiClase.variable_clase)

objeto01.variable_clase = "modificando variable de clase"
print(objeto01.variable_clase)
print(MiClase.variable_clase)

objeto02 = MiClase("Nuevo valor de instancia")
print(objeto02.variable_clase)

objeto03 = MiClase("Tercer Objeto")
MiClase.variable_clase = "Cambio desde la clase"

print(objeto01.variable_clase)
print(objeto02.variable_clase)
print(objeto03.variable_clase)