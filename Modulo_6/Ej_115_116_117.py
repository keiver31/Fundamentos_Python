'''
Ejercicio 115
Almacena en la variable ruta_base, un objeto Path que señale el directorio base del usuario.

Recuerda importar Path del módulo pathlib, y utilizar el método home()
'''
from pathlib import Path

ruta_base=Path.home()

'''
Ejercicio 116
Implementa y crea una ruta relativa que nos permita llegar al archivo "practicas_path.py" a partir de la siguiente estructura de carpetas:

Almacena el directorio obtenido en la variable ruta. No olvides importar Path.
'''
from pathlib import Path

ruta=Path("Curso Python","Día 6","practicas_path.py")

'''
Ejercicio 117
Implementa y crea una ruta absoluta que nos permita llegar al archivo "practicas_path.py" a partir de la siguiente estructura de carpetas:
Almacena el directorio obtenido en la variable ruta. No olvides importar Path, y de concatenar el objeto Path que refiere a la carpeta base del usuario.
'''
from pathlib import Path

base=Path.home()
ruta=Path(base,"Curso Python","Día 6","practicas_path.py")