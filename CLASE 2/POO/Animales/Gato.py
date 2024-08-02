
from Animal import Animal

# SUB CLASE
# CLASE HIJA
class Gato(Animal):
    def __init__(self, nombre, color):
        super().__init__(nombre)
        self.color = color
    
    def hablar(self):
        print("Miauu xd")
        print(f"Soy un gato miauu y mi nombre es: {self.nombre}, miauu y mi color es: {self.color}")