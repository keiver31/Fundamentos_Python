import numeros

def preguntar():
    
    print("Bienvenido a Farmacia Python")
    
    while True:
        print("[P] - PERFUMERIA\n[F] - FARMACIA\n[C] - COSMETICA")
        
        try:
            mi_rubro=input("Elija su opción ").upper()
            ["P","F","C"].index(mi_rubro)
        except ValueError:
            print("La opción indicada no es valida ")
        else:
            break
    
    numeros.decorador(mi_rubro)    
    
def inicio():
    
    while True:
        preguntar()
        
        try:
            otro_turno=input("Quieres sacar otro turno? [S] o [N] ").upper()
            ["S","N"].index(otro_turno)
        except ValueError:
            print("La opción indicada no es valida")
            
        else: 
            if otro_turno=="N":
                print("Gracias por su visita")
                break
            
inicio()
        