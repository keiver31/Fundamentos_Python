#Ejercicio 85
# Crea una lista valores_cuadrado formada por los números de la lista valores, elevados al cuadrado.
# valores = [1, 2, 3, 4, 5, 6, 9.5]
valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_cuadrado=[p**2 for p in valores]
print(valores_cuadrado)

#Ejercicio 86
# Crea una lista valores_pares formada por los números de la lista valores que (¡adivinaste!) sean pares.
# valores = [1, 2, 3, 4, 5, 6, 9.5]
valores = [1, 2, 3, 4, 5, 6, 9.5] 
valores_pares=[item for item in valores if item%2==0]
print(valores_pares)

#Ejercicio 87
# Para la siguiente lista de temperaturas en grados Fahrenheit, expresa estos mismos valores en una nueva lista de valores de temperatura en grados Celsius. La conversión entre tipo de unidades es la siguiente:
# °C = (°F - 32) * (5/9)
# o expresado de otro modo:
# (grados_fahrenheit-32)*(5/9)
# La lista de temperaturas es la siguiente:
# temperatura_fahrenheit = [32, 212, 275] 
# Almacena esta nueva lista en una variable llamada grados_celsius

temperatura_fahrenheit = [32, 212, 275]
grados_celsius=[((item-32)*(5/9)) for item in temperatura_fahrenheit]
print(grados_celsius)