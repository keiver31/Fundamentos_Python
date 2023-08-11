#Ejercicio 64:
# Utilizando loops For, saluda a todos los miembros de una clase, imprimiendo "Hola" + su nombre.
# Por ejemplo: "Hola María"
# alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]

alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]
for item in alumnos_clase:
    print("Hola "+item)
    
#Ejercicio 65:
# Dada la siguiente lista de números, realiza la suma de todos los números utilizando loops For y almacena el resultado de la suma en una variable llamada suma_numeros:
# lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_numeros =0

for item in lista_numeros:
    suma_numeros=item+suma_numeros

print(f"La suma total es: {suma_numeros} ")

#Ejercicio 66:
# Dada la siguiente lista de números, realiza la suma de todos los números pares e impares* por separado en las variables suma_pares y suma_impares respectivamente:
# lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
# *Recordando de los días anteriores: el módulo (o resto) de un número dividido 2 es cero cuando dicho valor es par, y 1 cuando es impar
# num % 2 == 0 (valores pares)
# num % 2 == 1 (valores impares)
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares =0

for item in lista_numeros:
    if item%2==0:
        suma_pares=suma_pares+item
    elif item%2==1:
        suma_impares=suma_impares+item

print(f"La suma de los pares es {suma_pares} y de los impares es {suma_impares}")
