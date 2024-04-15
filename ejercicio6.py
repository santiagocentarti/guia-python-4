while True:
    lado1=int(input("Ingrese el lado 1: "))
    lado2=int(input("Ingrese el lado 2: "))
    lado3=int(input("Ingrese el lado 3: "))

    if lado1+lado2>lado3 and lado1+lado3>lado2 and lado2+lado3>lado1:
        break
    else:
        print("Los lados del triangulo no son validos")
        
perimetro=lado1+lado2+lado3
semiperimetro=(lado1+lado2+lado3)/2
area=(semiperimetro*(semiperimetro-lado1)*(semiperimetro-lado2)*(semiperimetro-lado3))**.5

print(f"EL perimetro es {perimetro} y el area es {area}")