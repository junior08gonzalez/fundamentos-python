from Cuadrado import Cuadrado

#No es posible crear objetos de una clase abstracta
#figurageometrica = FiguraGeometrica()
cuadrado = Cuadrado(4, "rojo")
print(cuadrado.area())
print(cuadrado.get_color())

#print(Cuadrado.mro())