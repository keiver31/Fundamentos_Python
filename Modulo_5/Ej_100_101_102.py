'''
Ejercicio 100
Crea una función (lanzar_dados) que arroje dos dados al azar y devuelva sus resultados:

La función debe retornar dos valores resultado, que se encuentren entre 1 y 6).

Dicha función no debe requerir argumentos para funcionar, sino que debe generar internamente los valores aleatorios.

Proporciona el resultado de estos dos dados a una función que se llame evaluar_jugada (es decir, esta segunda función debe recibir dos argumentos) y que retorne -sin imprimirlo- un mensaje según la suma de estos valores:
Si la suma es menor o igual a 6:
"La suma de tus dados es {suma_dados}. Lamentable"
Si la suma es mayor a 6 y menor a 10:
"La suma de tus dados es {suma_dados}. Tienes buenas chances"
Si la suma es mayor o igual a 10:
"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"
Pistas: utiliza el método choice o randint de la biblioteca random para elegir un valor al azar entre 1 y 6.
'''
from random import *

def lanzar_dados():
    dado1=randint(1, 6)
    dado2=randint(1, 6)
    
    return dado1, dado2
    
def evaluar_jugada(dado1, dado2):
    suma_dados=dado1 + dado2
    
    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif suma_dados>6 and suma_dados<10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"


'''
Ejercicio 101
Crea una función llamada reducir_lista() que tome una lista como argumento (crea también la variable lista_numeros), y devuelva la misma lista, pero eliminando duplicados (dejando uno solo de los números si hay repetidos) y eliminando el valor más alto. El orden de los elementos puede modificarse.

Por ejemplo, si se le proporciona la lista [1,2,15,7,2] debe devolver [1,2,7].

Crea una función llamada promedio() que pueda recibir como argumento la lista devuelta por la anterior función, y que calcule el promedio de los valores de la misma. Debe devolver el resultado, sin imprimirlo.'''
lista_numeros=[0,2,2,-4,-4,8,10,7,5,6]
lista=[]
def reducir_lista(lista_numeros):
    contador=0
    for numero in lista_numeros:
        if numero not in lista: #Si no esta en la nueva lista, entonces agreguelo
            lista.append(numero)
            contador=contador+1
    lista.sort()
    lista.pop(-1)
     
        
    return lista

def promedio(lista_nueva):
    
    promedio=sum(lista_nueva)/len(lista_nueva)
    return promedio

#print(reducir_lista(lista_numeros))


'''
Ejercicio 102
Crea una función (llamada lanzar_moneda) que devuelva el resultado de lanzar una moneda (al azar). Dicha función debe poder devolver los resultados "Cara" o "Cruz", y no debe recibir argumentos para funcionar.
Crea una segunda función (llamada probar_suerte), que tome dos argumentos: el primero, debe ser el resultado del lanzamiento de la moneda. El segundo argumento, será una lista de números cualquiera (debes crear una lista con valores y llamarla lista_numeros).
Si se le proporciona una "Cara", debe mostrar el mensaje al usuario: "La lista se autodestruirá", y eliminarla (devolverla como lista vacía []).
Si se le proporciona una "Cruz", debe imprimir en pantalla: "La lista fue salvada" y devolver la lista intacta.
Pistas: utiliza el método choice de la biblioteca random para elegir un elemento al azar de una secuencia.
'''
import random

lista_numeros=[3,4,5,67,8,9]

def lanzar_moneda():
    lista=["Cara", "Cruz"]
    valor=random.choice(lista)
    print(valor)
    return valor
    
def probar_suerte(valor, lista_numeros):
    lista_nueva=[]
    if valor=="Cara":
        resultado="La lista se autodestruirá"
        lista_nueva=lista_nueva
    else:
        resultado="La lista fue salvada"
        lista_nueva=lista_numeros
    
    return lista_nueva
        


#valor=lanzar_moneda()
#respuesta, lista=probar_suerte(valor, lista_numeros)
#print(respuesta, lista)