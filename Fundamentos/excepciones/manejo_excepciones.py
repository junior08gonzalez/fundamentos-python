from numeros_identicos_exception import NumerosIdenticosException
resultado = None
try:
    a = int(input("Primer numero: "))
    b = int(input("Primer numero: "))
    if a==b:
        raise NumerosIdenticosException("Ocurrio un error numeros identicos")
    resultado = a/b
except Exception as e:
    print("Ocurrio un error", e)
    print(type(e))
except ZeroDivisionError as e:
    print("Ocurrio un error", e)
    print(type(e))
except TypeError as e:
    print("Ocurrio un error", e)
    print(type(e))
else:
    print("No hubo ninguna excepcion")
finally:
    print("Fin del manejo de excepciones")
print("Resultado: ", resultado)
