#Input
amount = int(input("Ingrese el monto: " ))
client = input("Ingrese el tipo de cliente, (G)General, (A)Afiliado: ")
t_pay = input("Ingrese el tipo de pago, (C)Contado, (P)Plazos: " )

if client == "G":
    if t_pay == "C":
        price = amount -((amount*15)/100)
        print("El precio teniendo en cuenta un descuento del 15% es de", price)
    else:
        value_periods = (amount*10)/100
        periods= amount/value_periods
        print("El valor del monto sera de", value_periods, "a", periods, "periodos")
else:
    if t_pay == "C":
        price = amount -((amount*20)/100)
        print("El precio teniendo en cuenta un descuento del 15% es de", price)
    else:
        value_periods = (amount*25)/100
        periods= amount/value_periods
        print("El valor del monto sera de", value_periods, "a", periods, "periodos")
