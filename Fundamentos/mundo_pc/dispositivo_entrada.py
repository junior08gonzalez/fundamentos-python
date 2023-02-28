class DispositivoEntrada:
    def __init__(self, marca, tipo_entrada):
        #atributos protegidos accesibles desde una sub clase
        self._marca = marca
        self._tipo_entrada = tipo_entrada