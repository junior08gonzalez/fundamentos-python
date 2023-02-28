a = int(input("Proporciona un valor: "))
valorMinimo = 0
valorMaximo = 5
dentroRango = (a >= valorMinimo and a <= valorMaximo)
#print(dentroRango)

if(dentroRango):
    print("dentro de rango")
else:
    print("fuera de rango")
    
vacaciones = False
diaDescanso = False
if(vacaciones or diaDescanso):
    print("Puedes ir al parque")
else:
    print("Tienes deberes que hacer")
    
#Invertir logica del algoritmo
#if(not(vacaciones or diaDescanso)):
#   print("Puedes ir al parque")
#else:
#    print("Tienes deberes que hacer")