from dispositivo_entrada import DispositivoEntrada

class Raton(DispositivoEntrada):
    contador_ratones = 0
    
    def __init__(self, marca, tipo_entrada):
        Raton.contador_ratones +=   1
        self.__id_raton = Raton.contador_ratones
        #acccedemos a los atributos protegidos
        self._marca = marca
        self._tipo_entrada = tipo_entrada
        
    def __str__(self):
        return (
            f"Id: {self.__id_raton}, "
            f"marca: {self._marca}, "
            f"tipo_entrada: {self._tipo_entrada}"
        )
        
raton = Raton("hp", "usb")
print(raton)