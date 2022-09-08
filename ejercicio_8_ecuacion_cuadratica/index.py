#Input
a = int(input("Ingrese un valor para a: "))
b = int(input("Ingrese un valor para b: "))
c = int(input("Ingrese un valor para c: "))
#Process
if a != 0:
    f_x = (-b + (b**2 - 4*a*c)**(1/2))/2*a
    s_x = (-b - (b**2 - 4*a*c)**(1/2))/2*a
    print("los puntos criticos son: ", f_x, "y", s_x)
else:
    print("(a) no puede ser cero")
     
