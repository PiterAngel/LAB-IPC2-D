

class usuario():
    # Constructor 
    def __init__(self, nombre, username, password):
        self.nombre = nombre
        self.username = username
        self.password = password
    
    # Encapsulamiento
    
    # ===== GETS ===== 
    def getNombre(self):
        return self.nombre
    
    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password
    
    # ===== SETS =====
    def setNombre(self, nombre):
        self.nombre = nombre

    def setUsername(self, username):
        self.username = username
    
    def setPassword(self, password):
        self.password = password