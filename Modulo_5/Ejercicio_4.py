'''
Escribe una función llamada contar_primos() que requiera un
solo argumento numérico.
Esta función va a mostrar en pantalla todos los números 
primos existentes en el rango que va desde cero hasta ese 
número incluido, y va a devolver la cantidad de números 
primos que encontró.
Aclaración, por convención el 0 y el 1 no se consideran primos
'''

def contar_primos(numero):
    
    primos =[2] #Inicia con dos
    iteracion=3 #Empieza chequeando desde 3
    
    if numero<2: #Si el usuario ingresa este numero no van a existir más primos
        return 0
    
    while iteracion<=numero:
        
        for n in range(3, iteracion, 2): #Avanza de 2 en 2 para omitir los pares
            if iteracion%n == 0:
                iteracion+=2 #Salto de 2 en 2
                break
        else:
            primos.append(iteracion)
            iteracion+=2 #Sigue con el loop while, para que no se detenga con el primero
            
    print(primos)
    return len(primos)

print(contar_primos(200))