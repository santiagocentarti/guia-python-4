nombre = input("Ingrese su nombre y verificaremos si es correcto: ")
apellido = input("Ingrese su apellido y verificaremos si es correcto: ")
numeros = ["1","2","3","4","5","6","7","8","9","0"]
bandera = 0
bandera2 = 0

for letra in nombre:
    if letra in numeros:
        print("El nombre es incorrecto porque tiene numeros")
        bandera = 1
if bandera == 0:
    print("El nombre es correcto")

for letra in apellido:
    if letra in numeros:
        print("El apellido es incorrecto porque tiene numeros")
        bandera2 = 1
if bandera2 == 0:
    print("El apellido es correcto")