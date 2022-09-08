#Input
t = int(input("Ingrese el tiempo en minutos de la llamada: "))
#Procces
if t <= 3:
    c = 300
else:
    c = ((t-3)*50) + 300 

#Output
print("Teniendo encuenta que la llamada duro", t, "el valor es de", c)
