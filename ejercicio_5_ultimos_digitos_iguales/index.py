#Input
number = int(input("Ingrese un numero: "))
#Procces
number %= 100
f_digit = number // 10
s_digit = number % 10

if f_digit == s_digit:
    print("los ultimos dos numeros son iguales")
else:
    print("El numero", f_digit, "no es igual que", s_digit)
