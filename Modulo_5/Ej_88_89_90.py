#Ejercicio 88
# Remueve los caracteres a la izquierda de nuestro texto principal:
# ,
# :
# %
# _
# #
# Utiliza el método lstrip(). Imprime el resultado en pantalla:
# ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"

texto=",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"
texto_check=texto.lstrip(",:%_#")
print(texto_check)

#Ejercicio 89
# Añade el elemento "naranja" como el cuarto elemento de la siguiente lista "frutas", utilizando
# el método insert():
# frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"] 
frutas.insert(3,"naranja")
print(frutas)

#Ejercicio 90
# Verifica si los sets a continuación forman conjuntos aislados (es decir, que no tienen elementos en común), utilizando el método isdisjoint(). Almacena dicho resultado en la variable conjuntos_aislados:
# marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
# marcas_tv = {"Sony", "Philips", "Samsung", "LG"}
marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}

marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

conjuntos_aislados=marcas_smartphones.isdisjoint(marcas_tv)

print(conjuntos_aislados)