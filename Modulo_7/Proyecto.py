class Persona:
    
    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido
        
        
class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance=0): #iniciar cuentas vacias
        super().__init__(nombre, apellido)
        self.numero_cuenta= numero_cuenta
        self.balance= balance
        
    def __str__(self):
        return f"Cliente:{self.nombre} {self.apellido}\Balance de cuenta {self.numero_cuenta}: ${self.balance}"    
    