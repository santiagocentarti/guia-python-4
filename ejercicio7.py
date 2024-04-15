a = float(input("Ingrese el primer numero: "))
b = float(input("Ingrese el primer numero: "))
c = float(input("Ingrese el primer numero: "))

discriminante = b**2 - 4 * a * c

if discriminante >= 0:
        x1 = (-b + (discriminante)**0.5) / (2*a)
        x2 = (-b - (discriminante)**0.5) / (2*a)
        print(f"Las raices del polinomio son: {x1} Y {x2}" )

elif discriminante < 0:
        print("Las raices son complejas")

elif discriminante == 0:
    x = -b / (2 * a)
    print("La raiz del polinomio es: ",x)