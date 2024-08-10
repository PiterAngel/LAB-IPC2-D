from click import pass_context
from Estudiante import Estudiante
from Profesor import Profesor
from Curso import Curso

#SE CREAN LOS ARREGLOS DE OBJETOS
Estudiantes = []
Profesores = []
Cursos = []


#SE CREAN LOS OBJETOS DE MANERA PREESTABLECIDA
#ESTUDIANTES
Estudiantes.append(Estudiante(20221,123456789,'Piter','Ciencias y Sistemas'))
Estudiantes.append(Estudiante(20222,123548458, 'Carlos','Mecanica'))
Estudiantes.append(Estudiante(20223,748661587, 'Juan', 'Industrial'))
#PROFESORES
Profesores.append(Profesor(1,'Pedro',781218467))
Profesores.append(Profesor(2,'Jose' ,785168778))
#CURSOS
Cursos.append(Curso('IPC 1', 5, 770))
Cursos.append(Curso('Logica de Sistemas', 2,789))
Cursos.append(Curso('IPC 2', 5, 771))
Cursos.append(Curso('Lenguajes Formales', 4, 796))

#MENU PRINCIPAL
def Menu():
    while(True):
        print("================================================================")
        print('Con que rol deseas entrar?:')
        print('1. Administrador')
        print('2. Estudiante')
        print('3. Profesor')
        print('4. Salir')
        opcion = input()
        if int(opcion) == 1:
            Menu_Admin()
        elif int(opcion) == 2:
            Ingresar_Estudiante()
        elif int(opcion) == 3:
            Ingresar_Profesor()
        elif int(opcion) == 4:
            break
        else:
            print('Selecciona una opcion correcta')

#INGRESAR COMO PROFESOR
def Ingresar_Profesor():
    print("================================================================")
    print('Ingrese su ID: ')
    id = int(input())
    if Verificar_Profesor(id) == True:
        Mostrar_Cursos()
    else:
        print('No puede ingresar')

#MOSTRAR TODOS LOS CURSOS CON LA CANTIDAD DE ESTUDIANTES
def Mostrar_Cursos():
    global Cursos
    print('=========CURSOS=========')
    for i in range(len(Cursos)):
        # CODIGO - NOMBRE = CANTIDAD_ESTUDIANTES
        print(str(Cursos[i].getCodigo()) + ' - ' + Cursos[i].getNombre() + ' = ' + str(Cursos[i].estudiantes))

#VERIFICA SI EXITE EL PROFESOR
def Verificar_Profesor(id):
    global Profesores
    for i in range(len(Profesores)):
        if id == Profesores[i].getId():
            return True
    return False

#VERIFICAR SI EXISTE EL ESTUDIANTE
def Verificar_Estudiante(id):
    global Estudiantes
    for i in range(len(Estudiantes)):
        if id == Estudiantes[i].getId():
            return True
    return False   

#INGRESAR COMO ESTUDIANTE
def Ingresar_Estudiante():
    print("================================================================")
    print('Ingrese su ID: ')
    id = int(input())
    if Verificar_Estudiante(id) == True:
        Menu_Estudiante(id)
    else:
        print('No puede ingresar')

#MENU ESTUDIANTE
def Menu_Estudiante(id):
    while(True):
        print("================================================================")
        print('Seleccione una opcion: ')
        print('1. Asignarme a un curso')
        print('2. Ver Cursos Asignados')
        print('3. Salir')
        opcion = int(input())
        if opcion == 1:
            Asignar_Curso(id)
        elif opcion == 2:
            Ver_Cursos_Asignados(id)
        elif opcion == 3:
            break
        else:
            print('Ingrese una opcion correcta')
    
#ASIGNAR UN CURSO A UN ESTUDIANTE
def Asignar_Curso(id):
    global Cursos
    print("================================================================")
    print('Escriba el codigo del curso al cual quiere asignarse:')
    print('=======LISTA DE CURSOS========')
    for i in range(len(Cursos)):
        # CODIG0 - NOMBRE (CREDITOS)
        print(str(Cursos[i].getCodigo()) + ' - ' + Cursos[i].getNombre()  + ' (' + str(Cursos[i].getCreditos()) + ')')

    codigo = int(input())
    if Retornar_Curso(codigo) != None:
        estudiante = Retornar_Estudiante(id)
        estudiante.cursos.append(Retornar_Curso(codigo))
        Retornar_Curso(codigo).estudiantes += 1
    else:
        print('Ingrese un codigo correcto')

#VER LOS CURSOS ASIGNADOS POR EL ESTUDIANTE
def Ver_Cursos_Asignados(id):
    estudiante = Retornar_Estudiante(id)
    print("================================================================")
    print('Estos son tus cursos asignados:')
    for i in range(len(estudiante.cursos)):
        # CODIG0 - NOMBRE (CREDITOS)
        print(str(estudiante.cursos[i].getCodigo()) + ' - ' + estudiante.cursos[i].getNombre()  + ' (' + str(estudiante.cursos[i].getCreditos()) + ')')



#RETORNAR EL CURSO
def Retornar_Curso(codigo):
    global Cursos
    for i in range(len(Cursos)):
        if codigo == Cursos[i].getCodigo():
            return Cursos[i]
    return None

#RETORNAR EL ESTUDIANTE
def Retornar_Estudiante(id):
    global Estudiantes
    for i in range(len(Estudiantes)):
        if id == Estudiantes[i].getId():
            return Estudiantes[i]

#MENU DE ADMINISTRADOR
def Menu_Admin():
    while(True):
        print("================================================================")
        print('Seleccione una opcion:')
        print('1. Crear Estudiante')
        print('2. Ver estudiantes')
        print('3. Crear Profesor')
        print('4. Ver Profesores')
        print('5. Salir')
        opcion = int(input())
        if opcion == 1:
            Crear_Estudiante()
        elif opcion == 2:
            Ver_Estudiantes()
        elif opcion == 3:
            Crear_Profesor()
        elif opcion == 4:
            Ver_Profesores()
        elif opcion == 5:
            break
        else:
            print('Selecciona una opcion correcta')

#CREAR UN ESTUDIANTE
def Crear_Estudiante():
    print("================================================================")
    nombre = input('Ingrese un nombre: ')
    id = int(input('Ingrese un ID para este estudiante: '))
    dpi = input('Ingrese el dpi del estudiante: ')
    carrera = input('Ingrese la carrera del estudiante: ')
    nuevo = Estudiante(id,dpi,nombre,carrera)
    Estudiantes.append(nuevo)
    print('Estudiante creado con exito')

#CREAR PROFESOR
def Crear_Profesor():
    print("================================================================")
    nombre = input('Ingrese un nombre: ')
    id = int(input('Ingrese un ID para este profesor: '))
    dpi = input('Ingrese el dpi del profesor: ')
    nuevo = Profesor(id,nombre,dpi)
    Profesores.append(nuevo)
    print('Profesor creado con exito')

#VER LA LISTA DE ESTUDIANTES
def Ver_Estudiantes():
    print("================================================================")
    global Estudiantes
    for i in range(len(Estudiantes)):
        print('=========================')
        print('     ESTUDIANTE')
        print('Nombre: ' + Estudiantes[i].getNombre())
        print('ID: ' + str(Estudiantes[i].getId()))
        print('DPI: ' + str(Estudiantes[i].getDpi()))
        print('Carrera: ' + str(Estudiantes[i].getCarrera()))

#VER LA LISTA DE PROFESORES
def Ver_Profesores():
    print("================================================================")
    global Profesores
    for i in range(len(Profesores)):
        print('--------------------------')
        print('     PROFESOR')
        print('Nombre: ' + Profesores[i].getNombre())
        print('ID: ' + str(Profesores[i].getId()))
        print('DPI: ' + str(Profesores[i].getDpi()))

#LLAMAR AL MENU PRINCIPAL
Menu()