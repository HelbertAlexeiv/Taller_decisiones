#Input
a = int(input("Ingrese un valor para a: "))
b = int(input("Ingrese un valor para b: "))

#Process
if a != 0:
    result = (-b/a)
else:
    print("No se puede dividir entre cero")
    result = 0

#Output
print("El valor de X es:", result)
