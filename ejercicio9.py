frase = input("Ingrese una frase: ") 
cantidadPalabras = 0  
bandera = False 

for i in frase:
    if i == ' ' and not bandera:
        cantidadPalabras += 1
        bandera = True
    elif i != ' ':  
        bandera = False

if not bandera:
    cantidadPalabras += 1

print("La cantidad de palabras en la frase es:", cantidadPalabras)  