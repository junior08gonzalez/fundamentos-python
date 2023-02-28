from figura_geometrica import FiguraGeometrica
from color import Color
class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, lado,ancho, color):
        FiguraGeometrica.__init__(self, lado , ancho)
        #super().__init__(lado,lado)
        Color.__init__(self,color)
        
    def area(self):
        return self.get_alto() * self.get_ancho()
    
    def __str__(self):
        return "Lado: "+self.get_alto() +" , ancho: "+self.get_ancho()+" , color: "+ self.get_color()
    