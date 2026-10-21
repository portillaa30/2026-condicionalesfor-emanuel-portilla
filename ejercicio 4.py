capital_c=int(input("Ingrese el capital c:"))
i=int(input("Ingrese la tasa anual:"))
m=int(input("Ingrese el entero M:"))

0<i<100
0<m<50

saldo=0
for año in range(m):
    interes_año=(saldo*i)/100
    saldo=saldo+capital_c
    saldo_nuevo=capital_c*(1+i/100)
if m==0:
    print(capital_c)


saldo_total= saldo_nuevo+interes_año

print(saldo_total)