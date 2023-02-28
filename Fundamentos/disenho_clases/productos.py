class Producto:
    contador_productos = 0
   
    def __init__(self, nombre, precio):
        
        Producto.contador_productos += 1
        self.__id_producto = Producto.contador_productos
        self.__nombre = nombre
        self.__precio = precio
    
    def get_precio(self):
        return self.__precio
    
    def set_precio(self, precio):
        self.__precio = precio
    
    
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    
    def __str__(self):
        return "Id Producto: "+str(self.__id_producto) + ", Nombre: "+self.__nombre +", Precio: "+\
            str(self.__precio)
            