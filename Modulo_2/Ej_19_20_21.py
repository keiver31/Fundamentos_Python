#Ejercicio 19:
"""Necesitamos imprimir el nombre y número de asociado dentro de la siguiente frase:

Estimado/a (nombre_asociado), su número de asociado es: (numero_asociado)"""

nombre_asociado = "Jesse Pinkman"
numero_asociado = 399058

print("Estimado/a {}, su número de asociado es: {}".format(nombre_asociado,numero_asociado ))


#Ejercicio 20:
# Muestra al usuario la cantidad de puntos acumulados dentro de la siguiente frase:

# Has ganado (puntos_nuevos) puntos! En total, acumulas (puntos_totales) puntos

puntos_nuevos = 350
puntos_totales = 1225

print(f"Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_totales} puntos")

#Ejercicio 21:
# Muestra al usuario la cantidad de puntos acumulados dentro de la siguiente frase:

# Has ganado (puntos_nuevos) puntos! En total, acumulas (puntos_totales) puntos

puntos_anteriores = 875
puntos_nuevos = 350

print(f"Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_anteriores+puntos_nuevos} puntos")