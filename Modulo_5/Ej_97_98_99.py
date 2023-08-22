'''
Ejercicio 97
Crea una función (todos_positivos) que reciba una lista de números como parámetro, y devuelva True si todos los valores de una lista son positivos, y False si al menos uno de los valores es negativo. Crea una lista llamada lista_numeros con valores positivos y negativos.
'''
lista_numeros=[20,30,40,-50,-200,100]

def todos_positivos(lista_numeros):
    
    for n in lista_numeros:
        
        if n<0:
            return False
        else:
            pass
        
    return True
    

'''
Ejercicio 98
Crea una función (suma_menores) que sume los números de una lista (almacenada en la variable lista_numeros) siempre y cuando sean mayores a 0 y menores a 1000, y devuelva el resultado de dicha suma.
'''
lista_numeros=[-30,20,101,239,45,67]


def suma_menores(lista_numeros):
    contador=0
    for n in lista_numeros:
        if n in range(1,1000):
            contador += n
        else:
            pass
    return contador

'''
Ejercicio 99
Crea una función (cantidad_pares) que cuente la cantidad de números pares que existen en una lista (lista_numeros), y devuelva el resultado de dicha cuenta.
'''
lista_numeros=[-30,20,101,239,45,67]


def cantidad_pares(lista_numeros):
    contador=0
    for n in lista_numeros:
        if n%2==0:
            contador += 1
        else:
            pass
    return contador