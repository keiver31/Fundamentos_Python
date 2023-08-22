'''

Escribe una función que requiera una cantidad indefinida de
argumentos. Lo que hará esta función es devolver True si en
algún momento se ha ingresado al numero cero repetido dos
veces consecutivas.
Por ejemplo:
(5,6,1,0,0,9,3,5) >>> True
(6,0,5,1,0,3,0,1) >>> False


'''

def search_consecutive(*args):
    contador=0
    for arg in args:
        if args[contador]==0 and args[contador+1]==0:
            return True
        else:
            contador+=1
    return False

result=search_consecutive(3,4,0,0,4,5)

if result==True:
    print(f"Se tienen dos 0 consecutivos")
else:
    print(f"No se tienen dos 0 consecutivos")
