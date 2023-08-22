'''
Ejercicio 118
Crea una función llamada abrir_leer() que abra (open) un archivo indicado como parámetro, y devuelva su contenido (read).
'''

def abrir_leer(archivo):
    archivo=open(archivo)
    lectura=archivo.read()
    return lectura

'''
Ejercicio 119
Crea una función llamada sobrescribir() que abra (open) un archivo indicado como parámetro, y sobrescriba cualquier contenido anterior por el texto "contenido eliminado"
'''
def sobrescribir(archivo):
    base=open(archivo, 'w')
    archivo=base.write("contenido eliminado")
    return archivo


'''
Ejercicio 120
Crea una función llamada registro_error() que abra (open) un archivo indicado como parámetro, y lo actualice añadiendo una línea al final que indique "se ha registrado un error de ejecución". Finalmente, debe cerrar el archivo abierto.
'''
def registro_error(archivo):
    base=open(archivo,'a')
    lectura= base.write("se ha registrado un error de ejecución")
    base.close()
    return lectura
