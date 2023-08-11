#Ejercicio 76
# Muestra en pantalla frases como la del siguiente ejemplo:
# La capital de Alemania es Berlín
# Utiliza la función zip, loops, y las siguientes listas de países y capitales para resolverlo rápida y eficientemente.
# capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
# paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]
capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

combinados=list(zip(capitales, paises))

for capital, pais in combinados:
    print(f"La capital de {pais} es {capital}")

#Ejercicio 77
# Crea un objeto zip formado a partir de listas, de un conjunto de marcas y productos que tú prefieras, dentro de la variable mi_zip.
marcas = ["Ford","Suzuki","Toyota"]
productos =["Carro", "Moto", "Camioneta"]
mi_zip=zip(marcas, productos)

#Ejercicio 78
# Crea el zip con las traducciones los números del 1 al 5 en español, portugués e inglés (en el mismo orden), y convierte el objeto generado en una lista almacenada en la variable numeros:
# uno / um / one
# dos / dois / two
# tres / três / three
# cuatro / quatro / four
# cinco / cinco / five
# El resultado deberá seguir la estructura:
# [('uno', 'um', 'one'), ('dos', 'dois', 'two'), ... ]
espanol=["uno", "dos", "tres", "cuatro", "cinco"]
ingles=["one","two","three","four","five"]
portugues=["um","dois","três","quatro","cinco"]

numeros=list(zip(espanol,portugues,ingles))