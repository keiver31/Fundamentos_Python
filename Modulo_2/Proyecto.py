nombre=input("Cual es su nombre? \n")
valor_ventas=input("Cual es el valor de las ventas de este mes?\n")

resultados_ventas=int(valor_ventas)
porcentaje_comision=13
comision=round((resultados_ventas*porcentaje_comision)/100, 3)

print(f"Las ventas de {nombre} este mes, fueron de {valor_ventas} COP y por lo tanto recibe una comisión de {comision} COP")
