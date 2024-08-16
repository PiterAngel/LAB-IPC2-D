
from xml.dom import minidom

doc = minidom.parse("C:\\Users\\Piter\\Desktop\\USAC\\SEGUNDO SEMESTRE 2024\\AUXILIATURA\\LAB IPC2\\REPO PUBLICO\\LAB-IPC2-D\\CLASE 4\\2.MINIDOM\\empleados.xml")

# Obtener el elemento raíz
empresa = doc.documentElement 

# Mostrar los departamentos y empleados
departamentos = empresa.getElementsByTagName("departamento")
for departamento in departamentos:
    nombre_departamento = departamento.getAttribute("departamento")
    print("Departamento: ", nombre_departamento)

    empleados = departamento.getElementsByTagName("empleado")
    for empleado in empleados:
        id_empleado = empleado.getAttribute("id")
        nombre = empleado.getElementsByTagName("nombre")[0].firstChild.data
        salario = empleado.getElementsByTagName("salario")[0].firstChild.data
        print(f"\t ID: {id_empleado}, Nombre: {nombre}, Salario: {salario} ")




