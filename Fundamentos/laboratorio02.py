class Caja:
    
    def __init__(self, largo, ancho, alto):
        self.largo = largo
        self.ancho = ancho
        self.alto = alto
        
    def calcularVolumen(self):
        volumen =  (self.largo * self.ancho * self.alto)
        return volumen
    
largo = int(input("INGRESAR EL LARGO DE LA CAJA: "))
ancho = int(input("INGRESAR EL ANCHO DE LA CAJA: "))
alto =  int(input("INGRESAR EL ALTO DE LA CAJA: "))
objecto = Caja(largo,ancho,alto)

print("La base del rectangulo es: ", objecto.calcularVolumen())