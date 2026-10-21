n=int(input("Insierte el numero de3 ciclistas:"))

menor_tiempo=float("inf")
minutos=""
centesimas=""
segundos=""

1<=n<=20

for r in range(n):
    registros=int(input("Ingrese el codigo de registro:"))
    centesimas=int(input("Ingresar marca en centesimas:"))
    segundos=int(input("Ingrese el tiempo en segundos:"))
    minutos=int(input("Ingresar marcas en minutos:"))

t=(60*minutos+segundos+centesimas)/100
velocidad=900/t

t_horas=t*3600
velocidad_km= t_horas* 0,25

if t<menor_tiempo:
    menor_tiempo=t
    ganador=registros

print("El ganadador ha sido", ganador,"con la marca de", menor_tiempo,"a la velociad de:", velocidad_km,)