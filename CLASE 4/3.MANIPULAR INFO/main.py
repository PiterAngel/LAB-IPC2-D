

import xml.etree.ElementTree as ET

# Mostrar todos los datos
def mostrar():

    arbol = ET.parse("C:\\Users\\Piter\\Desktop\\USAC\\SEGUNDO SEMESTRE 2024\\AUXILIATURA\\LAB IPC2\\REPO PUBLICO\\LAB-IPC2-D\\CLASE 4\\3.MANIPULAR INFO\\empleado.xml")
    raiz_empresa = arbol.getroot()

    print("Empresa")
    for departamento in raiz_empresa:
        print("Departamento: ", departamento.attrib['departamento'])
        for empleado in departamento:
            print("id: ", empleado.attrib['id'])
            print("nombre: ", empleado.findall("nombre")[0].text)
            print("salario: ", empleado.findall("salario")[0].text)
    
def actualizar():
    arbol = ET.parse("C:\\Users\\Piter\\Desktop\\USAC\\SEGUNDO SEMESTRE 2024\\AUXILIATURA\\LAB IPC2\\REPO PUBLICO\\LAB-IPC2-D\\CLASE 4\\3.MANIPULAR INFO\\empleado.xml")
    raiz_empresa = arbol.getroot()

    for departamento in raiz_empresa:
        for empleado in departamento:
            if (True):
                empleado.findall("nombre")[0].text = "nuevo nombre"
                print("datos actualizados")
    arbol.write("nuevoarchivo.xml")

def borrar():
    arbol = ET.parse("C:\\Users\\Piter\\Desktop\\USAC\\SEGUNDO SEMESTRE 2024\\AUXILIATURA\\LAB IPC2\\REPO PUBLICO\\LAB-IPC2-D\\CLASE 4\\3.MANIPULAR INFO\\empleado.xml")
    raiz_empresa = arbol.getroot()

    for departamento in raiz_empresa:
        empleados = list(departamento)  # Convertir a lista para poder modificar durante la iteración
        for empleado in empleados:
            departamento.remove(empleado)
            print("Datos eliminados")
    
    arbol.write("nuevoarchivo2.xml")


borrar()




