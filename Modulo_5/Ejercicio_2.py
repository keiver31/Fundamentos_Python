import random

'''
Escribe una función (puedes ponerle cualquier nombre que
quieras) que reciba cualquier palabra como parámetro, y que
devuelva todas sus letras únicas (sin repetir) pero en orden
alfabético.
Por ejemplo si al invocar esta función pasamos la palabra
"entretenido"
, debería devolver ['d'
,
'e'
,
'i'
,
'n'
,
'o'
,
'r'
,
't']
'''

def orden(palabra):
    
    lista_palabras=[]
    
    resultados=list(palabra)
    
    
    for resultados in resultados:
        if resultados not in lista_palabras:
            lista_palabras.append(resultados)
    
    lista_palabras.sort()
    
    return lista_palabras

lista=["parranguacutirimicary","definicion","ruina","estrategia","ataque"]
definicion=valor=random.choice(lista)
resultado=orden(definicion)
print(f"La palabra es {definicion} y el resultado es {resultado}")
#print(definicion)