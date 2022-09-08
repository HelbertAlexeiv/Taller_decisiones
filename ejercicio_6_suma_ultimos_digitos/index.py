#Input
number = int(input("Ingrese un numero: "))
#Procces
number %= 100
f_digit = number // 10
s_digit = number % 10
result = f_digit + s_digit


if result < 10:
    print("El resultado de los dos ultimos numeros es de un digito")
else:
    print("El resultado de los numeros", f_digit, "y", s_digit,"es", f_digit + s_digit, "por lo que no es de un digito")
