#Input
num = int(input("Ingrese un numero: "))
if num < 0:
    result = False
    print("El numero es negativo")
else:
    if num < 9999:
        print("El numero", num, "tiene cuatro digitos")
    else:
        print("El numero", num, "es mayor a cuatro digitos")


