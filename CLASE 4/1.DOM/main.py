from xml.dom import Node
from xml.dom import minidom

doc = minidom.parse("C:\\Users\\Piter\\Desktop\\USAC\\SEGUNDO SEMESTRE 2024\\AUXILIATURA\\LAB IPC2\\REPO PUBLICO\\LAB-IPC2-D\\CLASE 4\\1.DOM\\empleados.xml")


# elemento raiz
empresa = doc.documentElement

# Mostrar los departamentos y empleados

for node in empresa.childNodes:
    if node.nodeType == node.ELEMENT_NODE and node.tagName == "departamento":
        nombre_departamento = node.getAttribute("departamento")
        print("Departamento: " , nombre_departamento)


        for empleado_node in node.childNodes:
            if empleado_node.nodeType == node.ELEMENT_NODE and empleado_node.tagName == "empleado":
                id_empleado = empleado_node.getAttribute("id")

                nombre = None
                salario = None
                for mini in empleado_node.childNodes:
                    if mini.nodeType == node.ELEMENT_NODE:
                        if mini.tagName == "nombre":
                            nombre = mini.firstChild.data
                        elif mini.tagName == "salario":
                            salario = mini.firstChild.data
        print(f"\t ID: {id_empleado}, Nombre: {nombre}, Salario: {salario}" )

