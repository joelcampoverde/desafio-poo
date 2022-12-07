import math

print("distancia de entrega")

x1=float(input("ingresa entrega1: "))
y1=float(input("ingresa entrega2: "))
x2=float(input("ingresa entrega3: "))
y2=float(input("ingresa entrega4: "))

x=x2 - x1
y=y2 - y1
d=math.sqrt(x**2+y**2)
print("la distancia sera:  {0:4f}".format(d))