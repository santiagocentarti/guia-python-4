edad = int(input("Ingrese su edad para validar si es apto para solicitar la jubilación: "))
if edad >= 65:
    print("Usted es apto para cobrar la jubilacion.")
else:
    print("Usted no es apto para cobrar la jubilacion.")
    edadfaltante= 65-edad
    print(f"A usted le faltan {edadfaltante} años, para solicitar la jubilacion")