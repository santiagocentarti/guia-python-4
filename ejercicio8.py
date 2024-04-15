email = input("Ingrese su mail: ")

for i in email:
    if "@" in email and len(email)<255:
        print("El email es valido")
        break
    else:
        print("El email no es valido")
        break