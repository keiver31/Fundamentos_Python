'''
Ejercicio 103
Crea una función llamada suma_cuadrados que tome una cantidad indeterminada de argumentos numéricos, y que retorne la suma de sus valores al cuadrado.

Por ejemplo para los argumentos suma_cuadrados(1,2,3) deberá retornar 14 (1+4+9).
'''
def suma_cuadrados(*args):
    total=0
    for arg in args:
        cuadrado=arg**2
        total =total+cuadrado
        
    return total
    
#suma_cuadrados(1,4,57,89)
#print(suma_cuadrados)


'''
Ejercicio 104
Crea una función llamada suma_absolutos, que tome un conjunto de argumentos de cualquier extensión, y retorne la suma de sus valores absolutos (es decir, que tome los valores sin signo y los sume, o lo que es lo mismo, los considere a todos -negativos y positivos- como positivos).
'''
def suma_absolutos(*args):
    total=0
    for arg in args:
        absoluto=abs(arg)
        total += absoluto
    
    return total

'''
Ejercicio 105
Crea una función llamada numeros_persona que reciba, como primer argumento, un nombre, y a continuación, una cantidad indefinida de números.

La función debe devolver el siguiente mensaje:

"{nombre}, la suma de tus números es {suma_numeros}"'''
def numeros_persona(nombre, *numeros):
    suma_numeros=0
    for numero in numeros:
        suma_numeros += numero
    
    mensaje=f"{nombre}, la suma de tus números es {suma_numeros}"
        
    return mensaje