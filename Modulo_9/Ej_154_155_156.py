'''
Ejercicio 154

Crea un objeto fecha llamado mi_fecha que almacene el día 3 de febrero de 1999
'''
import datetime

mi_fecha=datetime.date(1999, 2, 3)

'''
Ejercicio 155
Crea un objeto en la variable hoy que siempre almacene la fecha actual cuando sea invocada.
'''
import datetime

hoy=datetime.date.today()

'''
Ejercicio 156
En una variable llamada minutos, almacena únicamente los minutos de la hora actual.

Por ejemplo, si se ejecutara a las 20:43:17 de la noche, la variable minutos debe almacenar el valor 43
'''
import datetime

ahora=datetime.datetime.today()
minutos=ahora.minute