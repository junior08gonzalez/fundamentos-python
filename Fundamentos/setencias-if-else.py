condicion = True

print("Condicion verdadera01") if condicion else print("Condicion falsa01")

if condicion:
    print("La condicion es verdadera")
else:
    print("La condicion es falsa")
    
numero = int(input("Proporciona un numero entre 1 y 3:"))

if numero == 1:
    numeroTexto = "numero uno"
elif numero == 2:
    numeroTexto = "numero dos"
elif numero == 3:
    numeroTexto = "numero tres"
else:
    numeroTexto = "Valor fuera de rango"

print("numero proporcionado: "+numeroTexto)