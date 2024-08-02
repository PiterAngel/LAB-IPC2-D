
# SUPER CLASE
class Persona:
    def __init__(self, nombre, apellido, edad, genero): # CONSTRUCTOR
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.genero = genero
    
    def hablar(self):
        print("Hola soy una persona recien creada, soy un robot :)")