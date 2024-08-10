

class Curso():
    def __init__(self, nombre, creditos, codigo):
        self.nombre = nombre
        self.creditos = creditos
        self.codigo = codigo
        self.profesor = None
        self.estudiantes = 0
    
    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre
    
    def getCreditos(self):
        return self.creditos
    
    def setCreditos(self, creditos):
        self.creditos = creditos

    def getCodigo(self):
        return self.codigo
    
    def setCodigo(self, codigo):
        self.codigo = codigo