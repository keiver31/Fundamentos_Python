'''
Y así hemos terminado la parte preparatoria de este 5º día de entrenamiento y ahora vamos 
a poner toda la carne en la parrilla porque se viene un desafío más que especial. Hoy vas a 
programar El Ahorcado. El juego es muy sencillo y popular, pero por si acaso te lo explico 
rápidamente. 
El programa va a elegir una palabra secreta y le va a mostrar al jugador solamente una serie 
de guiones que representa la cantidad de letras que tiene la palabra. El jugador en cada turno 
deberá elegir una letra y si la letra se encuentra en la palabra oculta, el sistema le va a 
mostrar en qué lugares se encuentra. Pero si el jugador dice una letra que no se encuentra en 
la palabra oculta, pierde una vida.
En el juego real del ahorcado, cada vez que perdemos una vida, se va completando el dibujo 
del ahorcado miembro por miembro. Pero en nuestro caso, como aún no tenemos elementos 
gráficos, simplemente le vamos a decir que tiene seis vidas y se las iremos descontando de una 
en una, cada vez que el jugador elija una letra incorrecta. 
Si se agotan las vidas antes de adivinar la palabra, el jugador pierde. Pero si adivina la palabra 
completa antes de perder todas las vidas, el jugador gana. 
Parece sencillo, pero ¿cómo diseñamos todo este código? Bueno, aquí van algunas ayudas: 
 Primero vas a crear un código que importe el método choice, ya que lo vas a necesitar 
para que el sistema pueda elegir una palabra al azar dentro de una lista de palabras que 
también vas a crear al comienzo. 
 Luego de eso, vas a crear tantas funciones como creas necesarias para que el programa 
haga cosas como pedirle al usuario que elija una letra, para corroborar si lo que el usuario 
ha ingresado es una letra válida, para chequear si la letra ingresada se encuentra en la 
palabra o no, para verificar si ha ganado o no, etc. 
 Recuerda escribir primero las funciones y luego el código que las implementa 
ordenadamente. 
'''
from random import choice

palabras=['supreme','rana', 'huerfano','validador']
letras_correctas=[]
letras_incorrectas=[]
intentos=6
aciertos=0
juego_terminado=False

def elegir_palabra(lista_palabras):
    palabra_elegida=choice(lista_palabras)
    letras_unicas = len(set(palabra_elegida))
    
    return palabra_elegida, letras_unicas

def pedir_letra():
    letra_elegida=''
    es_valida=False
    abecedario='abcdefghijklmnñopqrstuvwxyz'
    
    while not es_valida:
        letra_elegida=input("Elige una letra: ").lower()
        
        if letra_elegida in abecedario and len(letra_elegida)==1:
            es_valida=True
        else:
            print("No has elegido una letra correcta")
            
    return letra_elegida

def mostrar_nuevo_tablero(palabra_elegida):
    lista_oculta=[]
    
    for l in palabra_elegida:
        if l in letras_correctas:
            lista_oculta.append(l)
        else:
            lista_oculta.append('-')
    print('-'.join(lista_oculta))
    
def chequear_letra(letra_elegida, palabra_oculta, vidas, coincidencias):
    
    fin=False
    
    if letra_elegida in palabra_oculta and letra_elegida not in letras_correctas:
        letras_correctas.append(letra_elegida)
        coincidencias +=1
    elif letra_elegida in palabra_oculta and letra_elegida in letras_correctas:
        print("Ya has encontrado esa letra, prueba con otra diferente")
    else:
        letras_incorrectas.append(letra_elegida)
        vidas -=1
    
    if vidas==0:
        fin=perder()
    elif coincidencias == letras_unicas:
        fin= ganar(palabra_oculta)
        
    return vidas, fin, coincidencias

def perder():
    print("Te has quedado sin vida")
    print("La palabra oculta era "+palabra)
    
    return True

def ganar(palabra_descubierta):
    mostrar_nuevo_tablero(palabra_descubierta)
    print("Felicitaciones, has encontrado la palabra!!!")
    
    return True

palabra, letras_unicas=elegir_palabra(palabras)

while not juego_terminado:
    print('\n' +'*'*20+ '\n')
    mostrar_nuevo_tablero(palabra)
    print('\n')
    print('Letras incorrectas: '+'-'.join(letras_incorrectas))
    print(f"Vidas: {intentos}")
    print('\n' +'*'*20+ '\n')
    letra=pedir_letra()
    
    intentos, terminado, aciertos=chequear_letra(letra, palabra, intentos, aciertos)
    juego_terminado =terminado