terminoA=int(input("Ingrese el primer termino a:"))
diferenciaD=int(input("Ingrese la diferencia D: "))
cantidadN=int(input("Ingrese la cantidad N: "))

"""
terminoA and diferenciaD(range(-100,100))
cantidadN(range(0,1000))

if cantidadN==0:
    print("El total es cero")
else:
    for suma in range(terminoA,terminoA+diferenciaD,cantidadN):
"""

t = terminoA
s = 0
for k in range(1, cantidadN+1):
    s = s + t
    t = t + diferenciaD

print(s)
