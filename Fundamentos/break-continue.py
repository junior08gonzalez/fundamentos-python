#Imprimir solo las letras a
for letra in "Holanda":
    if letra == "a":
        print(letra)
        break
else:
    print("Fin ciclo for")
    
#Imprimir solo numeros pares
#for i in range(6):
#    if i % 2 == 0 :
#        print(i)
        
for i in range(6):
    if i % 2 != 0 :
        continue
    print(i)