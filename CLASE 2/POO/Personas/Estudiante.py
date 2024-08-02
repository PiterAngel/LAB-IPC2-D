
from Persona import Persona

class Estudiante(Persona):

    def setCarnet(self, carnet):
        self.carnet = carnet
    
    def getCarnet(self):
        return self.carnet

    def hablar(self):
        print("Buenas tardes, soy un estudiante de inge :)")
        print("Mi nombre es: ", self.nombre)
        print(f"Mi nombre es: {self.nombre}, y mi apellido es {self.apellido}")