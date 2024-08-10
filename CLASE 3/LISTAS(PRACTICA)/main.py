# importar archivos 
from usuario import usuario

#LISTA
usuarios = []

usuario1 = usuario("Piter", "aux", "1999")
usuario2 = usuario("Angel", "aux2", "2000")

# el append nos permite agregar componentes a la lista /*/*/*/ SOLO PARA PRACTICA /*//*/*/*
usuarios.append(usuario1)
usuarios.append(usuario2)

for i in range(len(usuarios)):
    print("======================================")
    print("Nombre: " + usuarios[i].getNombre())
    print("Username: "+ usuarios[i].getUsername())
    print("Password: "+ usuarios[i].getPassword())


