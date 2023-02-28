class Rectangulo:
    
    def __init__(self, altura, base):
        self.altura = altura
        self.base = base
        
    def calcularArea(self):
        area =  (self.base * self.altura)
        return area
    
base = int(input("INGRESAR LA BASE DEL RECTANGULO: "))
altura = int(input("INGRESAR LA ALTURA DEL RECTANGULO: "))

objecto = Rectangulo(altura,base)

print("La base del rectangulo es: ", objecto.calcularArea())