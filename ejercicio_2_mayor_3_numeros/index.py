#input
a = int(input("Ingrese el primer numero entero:"))
b = int(input("Ingrese el segundo numero entero:"))
c = int(input("Ingrese el tercer numero entero:"))

#Process

if a>b:
    if a>c:
        mayor = a
        mitad = c
        menor = b
    else:
        mayor = c
        mitad = a
        menor = b
else:
    if b>c:
        mayor = b
        mitad = c
        menor = a
    else:
        mayor = c
        mitad = b
        menor = a

print(menor, mitad, mayor)
