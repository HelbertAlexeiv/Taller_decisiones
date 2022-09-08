# Processing / Output
a = int(input("Escriba el primer numero:"))
b = int(input("Escriba el segundo numero:"))
c = int(input("Escriba el tercer numero:"))
if a > b:
    if a > c:
        if b > c:
            print("Los tres números organizados de forma ascendente sería la siguiente:", a, b, c)
        else:
            print("Los tres números organizados de forma ascendente sería la siguiente:", a, c, b)
    else:
        print("Los tres números organizados de forma ascendente sería la siguiente:", c, a, b)
else:
    if a > c:
        print("Los tres números organizados de forma ascendente sería la siguiente:", b, a, c)
    else:
        if b > c:
            print("Los tres números organizados de forma ascendente sería la siguiente:", a, c, b)
        else:
            print("Los tres números organizados de forma ascendente sería la siguiente:", c, b, a)
