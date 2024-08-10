
class Profesor():
    def __init__(self, id, nombre, dpi):
        self.id = id
        self.nombre = nombre
        self.dpi = dpi
    
    def getId(self):
        return self.id
    
    def setId(self, id):
        self.id = id

    def getNombre(self):
        return self.nombre
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def getDpi(self):
        return self.dpi
    
    def setDpi(self, dpi):
        self.dpi = dpi