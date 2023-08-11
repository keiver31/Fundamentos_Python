"""La consigna es la siguiente: vas a crear un programa que primero le pida al usuario que 
ingrese un texto. Puede ser un texto cualquiera: un artículo entero, un párrafo, una frase, un 
poema, lo que quiera. Luego, el programa le va a pedir al usuario que también ingrese tres 
letras a su elección y a partir de ese momento nuestro código va a procesar esa información 
para hacer cinco tipos de análisis y devolverle al usuario la siguiente información: """

#Ingreso datos
texto=input("Ingrese un texto cualquiera(Ej:artículo entero, un párrafo, una frase, un poema, lo que quiera)?\n")
letra_1=input("Ingrese una letra cualquiera\n")
letra_2=input("Ingrese una letra cualquiera\n")
letra_3=input("Ingrese una letra cualquiera\n")

#Estandarizo los datos
texto_mod=texto.lower()
letra_1_mod=letra_1.lower()
letra_2_mod=letra_2.lower()
letra_3_mod=letra_3.lower()
print(type(texto_mod))


"""
1. Primero: ¿cuántas veces aparece cada una de las letras que eligió? Para lograr esto, te 
recomiendo almacenar esas letras en una lista y luego usar algún método propio de string 
que nos permita contar cuantas veces aparece un sub string dentro del string. Algo que 
debes tener en cuenta es que al buscar las letras pueden haber mayúsculas y minúsculas 
y esto va a afectar el resultado. Lo que deberías hacer para asegurarte de que se 
encuentren absolutamente todas las letras es pasar, tanto el texto original como las 
letras a buscar, a minúsculas. 
"""
#Guardo los datos en una lista para luego buscarlos
text_search=[letra_1_mod,letra_2_mod,letra_3_mod]
print("Solución del punto #1: Cantidad de letras repetidas")
#Procedo a buscar los datos y a imprimirlos
#Letra 1
busq_1=texto_mod.count(text_search[0])
print(f"La letra {letra_1} aparece {busq_1} veces")
#Letra 2
busq_2=texto_mod.count(text_search[1])
print(f"La letra {letra_2} aparece {busq_2} veces")
#Letra 3
busq_3=texto_mod.count(text_search[2])
print(f"La letra {letra_3} aparece {busq_3} veces\n")


"""
2. Segundo: le vas a decir al usuario cuántas palabras hay a lo largo de todo el texto. Y 
para lograr esta parte, recuerda que hay un método de string que permite transformarlo 
en una lista y que luego hay una función que permite averiguar el largo de una lista. 
"""
print("Solución del punto #2: Cantidad de palabras")

palabras= texto_mod.split()
total_palabras=len(palabras)
print(f"La cantidad de palabras ingresadas en el texto, es de {total_palabras}\n")

"""
3. Tercero: nos va a informar cuál es la primera letra del texto y cuál es la última. Aquí 
claramente echaremos mano de la indexación. 
"""
print("Solución del punto #3: Primera y última letra del texto")
primer_letra=texto[0]
ultima_letra=texto[-1]
print(f"La primer letra del texto es la '{primer_letra}' y la última letra es '{ultima_letra}'\n")


"""
4. Cuarto: el sistema nos va a mostrar cómo quedaría el texto si invirtiéramos el orden de 
las palabras. ¿Acaso hay algún método que permita invertir el orden de una lista, y otro 
que permita unir esos elementos con espacios intermedios? Piénsalo. 
"""
print("Solución del punto #4: Invirtiendo el orden de las palabras")
palabras.reverse()
texto_inv=' '.join(palabras)
print(f"El texto invertido es el siguiente\n '{texto_inv}'\n")


"""
5. Y por último: el sistema nos va a decir si la palabra “Python” se encuentra dentro del 
texto. Esta parte puede ser algo complicada de imaginársela, pero te voy a dar una pista: 
puedes usar booleanos para hacer tu averiguación y un diccionario para encontrar la 
manera de expresarle al usuario tu respuesta.
"""
print("Solución del punto #5: Buscando la palabra 'Python' en el texto")

buscador="python" in texto_mod
busqueda_dic={True:"si",False:"no"}
print(f"La palabra 'Python' {busqueda_dic[buscador]} se encuentra en el texto")