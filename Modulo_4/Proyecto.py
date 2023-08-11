# La consigna es esta: el programa le va a preguntar al usuario su nombre, y luego le va a decir 
# algo así como “Bueno, Juan, he pensado un número entre 1 y 100, y tienes solo ocho intentos 
# para adivinar cuál crees que es el número”. Entonces, en cada intento el jugador dirá un 
# número y el programa puede responder cuatro cosas distintas: 

# Si el número que dijo el usuario es menor a 1 o superior a 100, le va a decir que ha elegido 
# un número que no está permitido. 
#  Si el número que ha elegido el usuario es menor al que ha pensado el programa, le va a 
# decir que su respuesta es incorrecta y que ha elegido un número menor al número secreto. 
#  Si el usuario eligió un número mayor al número secreto, también se lo hará saber de la 
# misma manera. 
#  Y si el usuario acertó el número secreto, se le va a informar que ha ganado y cuántos 
# intentos le ha tomado. 
# Si el usuario no ha acertado en este primer intento, se le va a volver a pedir que elija otro 
# número. Y así hasta que gane o hasta que se agoten los ocho intentos. 

from random import *

intentos_usuario=0
contador=0
intento=0

numero_secreto=randint(1,100)

usuario=input("Cual es el nombre del usuario?\n")
print(f"Bueno {usuario}, he pensado un número entre 1 y 100, y tienes solo ocho intentos para adivinar cuál crees que es el número")


while intentos_usuario<8:

    intento=int(input("Ingrese el numero para el intento:\n"))
    intentos_usuario=intentos_usuario+1
    
    if intento<0 or intento>100:
        print("El numero ingresado no esta permitido")
    elif intento<numero_secreto:
        print("Mi numero es más alto")
    elif intento>numero_secreto:
        print("Mi numero es más bajo")
    elif intento == numero_secreto:
        print(f"Felicitaciones {usuario}! Has adivinada en {intentos_usuario} intentos")
        break
    
if intento != numero_secreto:
    print(f"Lo siento, se han agotado los intentos. El numero secreto era {numero_secreto}")
        
    