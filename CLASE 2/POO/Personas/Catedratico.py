# IMPORTAR LAS QUE ESTAMOS UTILIZANDO
from Persona import Persona


# SUBCLASE
class Catedratico(Persona):

    def setSalon(self, salon):
        self.salon = salon
    
    def getSalon(self):
        return self.salon

    def hablar(self):
        print("Buenas tardes, soy su profesor :)")
        print("Mi nombre es: ", self.nombre)
        print(f"Mi nombre es: {self.nombre}, y mi apellido es {self.apellido}")
 
