frase=input("Ingrese una frase: ")
vocales=0
consonantes=0

for i in frase:
    if i=="a" or i=="e" or  i=="i" or i=="o" or i=="u":
        vocales+=1
    else:
        consonantes+=1
print("La cantidad de vocales de la frase es: ",vocales)
print("La cantidad de consonantes de la frase es: ",consonantes)