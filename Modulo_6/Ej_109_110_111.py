'''
Ejercicio 109
Abre el archivo texto.txt e imprime su contenido.

Nota: el archivo se encuentra guardado en la misma carpeta donde se aloja tu código
'''
mi_archivo=open('texto.txt')
print(mi_archivo.read())

'''
Ejercicio 110
Imprime la primera línea del archivo texto.txt

No olvides abrir el archivo y cerrarlo luego de ejecutar tu código.

Nota: el archivo se encuentra guardado en la misma carpeta donde se aloja tu código
'''
mi_archivo=open('texto.txt')
linea=mi_archivo.readline()
print(linea)

mi_archivo.close()

'''
Ejercicio 111
Abre el archivo texto.txt e imprime únicamente la segunda línea.
'''
mi_archivo=open('texto.txt')
linea=mi_archivo.readlines()
print(linea[1])

mi_archivo.close()