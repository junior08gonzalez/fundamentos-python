#ABC = Abstract Base Class
from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    def __init__(self, ancho, alto):
        self.__ancho = ancho
        self.__alto = alto
    def get_alto(self):
        return self.__alto
    
    def set_alto(self,alto):
        self.__alto = alto
        
    def get_ancho(self):
        return self.__ancho
    
    def set_ancho(self,ancho):
        self.__ancho = ancho
        
    @abstractmethod    
    def area(self):
        pass