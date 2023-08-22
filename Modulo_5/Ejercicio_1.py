import random
'''
Crea una función llamada devolver_distintos() que reciba 3
integers como parámetros.
Si la suma de los 3 numeros es mayor a 15, va a devolver el
número mayor.
Si la suma de los 3 numeros es menor a 10, va a devolver el
número menor.
Si la suma de los 3 números es un valor entre 10 y 15
(incluidos) va a devolver el número de valorintermedio.
'''

def devolver_distintos(*args):
    lista=[]
    
    numeros=f"Los numeros son {args} "

    for arg in args:
        lista.append(arg)
      
      
    suma=sum(lista)
    if suma>15:
        valor=max(lista)
        mensaje=f"y el maximo es {valor}"
    elif suma<10:
        valor=min(lista)
        mensaje=f"y el minimo es {valor}"
    elif suma>=10 and suma<=15:
        lista.sort()
        valor=lista[1]
        mensaje=f"y el intermedio es {valor}"
        
        
    return numeros, mensaje

valor1=int(random.randint(1,3))
valor2=int(random.randint(4,7))
valor3=int(random.randint(2,9))
valores, resultado=devolver_distintos(valor1,valor2,valor3)
print(valores+resultado)