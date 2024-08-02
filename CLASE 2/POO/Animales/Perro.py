
from Animal import Animal 

# SUB CLASE
# CLASE HIJA
class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza
    
    def hablar(self):
        print("Guauuu xd")
        print(f"Mi nombre es: {self.nombre}, guauu, soy raza: {self.raza}")
    
    
