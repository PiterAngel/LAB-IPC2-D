# PARA LAS INSTANCIAS 
# persona100 = Persona("Juan", 30)

from Catedratico import Catedratico
from Estudiante import Estudiante

profesor100 = Catedratico("Stanley", "Barrios", 30, "masculino")
profesor100.hablar()
profesor100.setSalon(305)
print("mi salon es: ", profesor100.getSalon())

print("================================================================")

estudiante200 = Estudiante("Angel", "Zea", 20, "masculino")
estudiante200.hablar()
estudiante200.setCarnet(2020)
print("mi Carnet es: ", estudiante200.getCarnet())