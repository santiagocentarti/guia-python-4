nombre1=input("ingrese un nombre: ")
nombre2=input("ingrese el segundo nombre: ")
nombre3=input("ingrese el tercer nombre: ")
nombre4=input("ingrese el cuarto nombre: ")
nombre5=input("ingrese el quinto nombre: ")
nombre6=input("ingrese el sexto nombre: ")
nombre7=input("ingrese el septimo nombre: ")

nums=["1","2","3","4","5","6","7","8","9","0"]

nombres=[nombre1,nombre2,nombre3,nombre4,nombre5,nombre6,nombre7]

bandera=0
for i in nombres:
    for f in i:
        if f in nums:
            bandera=1
            break
    if bandera==1:
        print("Un nombre contiene numeros")
        break
    
names=sorted(nombres)
if names!=nombres:
    bandera=1
    print("La lista no estaba en orden alfabetica")
if bandera==0:
    print("Todo fue ingresado correctamente")