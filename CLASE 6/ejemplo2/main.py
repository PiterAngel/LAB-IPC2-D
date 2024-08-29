import xml.etree.ElementTree as ET
from xml.dom import minidom
import graphviz

# Clase NodoEmpleado para lista doblemente enlazada
class NodoEmpleado:
    def __init__(self, nombre, puesto, sueldo):
        self.nombre = nombre
        self.puesto = puesto
        self.sueldo = sueldo
        self.siguiente = None
        self.anterior = None  # Referencia al nodo anterior

# Clase NodoEmpresa
class NodoEmpresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados_primero = None
        self.empleados_ultimo = None
        self.siguiente = None

    def agregar_empleado(self, nombre, puesto, sueldo):
        nuevo_empleado = NodoEmpleado(nombre, puesto, sueldo)
        if not self.empleados_primero:
            self.empleados_primero = nuevo_empleado
            self.empleados_ultimo = nuevo_empleado
        else:
            nuevo_empleado.anterior = self.empleados_ultimo  # Enlace al anterior
            self.empleados_ultimo.siguiente = nuevo_empleado
            self.empleados_ultimo = nuevo_empleado

# Clase ListaCircularEmpresas
class ListaCircularEmpresas:
    def __init__(self):
        self.primera_empresa = None
        self.ultima_empresa = None

    def agregar_empresa(self, nombre):
        nueva_empresa = NodoEmpresa(nombre)
        if not self.primera_empresa:
            self.primera_empresa = nueva_empresa
            self.ultima_empresa = nueva_empresa
            self.ultima_empresa.siguiente = self.primera_empresa
        else:
            self.ultima_empresa.siguiente = nueva_empresa
            self.ultima_empresa = nueva_empresa
            self.ultima_empresa.siguiente = self.primera_empresa

    def cargar_desde_xml(self, ruta_xml):
        tree = ET.parse(ruta_xml)
        root = tree.getroot()

        for empresa_element in root.findall('empresa'):
            nombre_empresa = empresa_element.find('nombre').text
            self.agregar_empresa(nombre_empresa)

            empresa_actual = self.ultima_empresa
            empleados_element = empresa_element.find('empleados')

            for empleado_element in empleados_element.findall('empleado'):
                nombre_empleado = empleado_element.find('nombre').text
                puesto = empleado_element.find('puesto').text
                sueldo = empleado_element.find('sueldo').text
                empresa_actual.agregar_empleado(nombre_empleado, puesto, sueldo)

    def generar_grafico(self, ruta_grafico):
        dot = graphviz.Digraph(comment='Empresas y Empleados')

        # Nodo inicial con cantidad de empresas
        cantidad_empresas = self.contar_empresas()
        cantidad_empleados = self.contar_empleados_total()
        dot.node('Empresas', f'Empresas\n(x={cantidad_empresas}, y={cantidad_empleados})')

        actual_empresa = self.primera_empresa
        while True:
            dot.node(actual_empresa.nombre, actual_empresa.nombre)
            dot.edge('Empresas', actual_empresa.nombre)

            actual_empleado = actual_empresa.empleados_primero
            while actual_empleado:
                empleado_label = f'{actual_empleado.nombre}\nPuesto: {actual_empleado.puesto}\nSueldo: {actual_empleado.sueldo}'
                dot.node(actual_empleado.nombre, empleado_label)

                # Enlace entre empresa y el primer empleado
                if actual_empleado == actual_empresa.empleados_primero:
                    dot.edge(actual_empresa.nombre, actual_empleado.nombre)

                # Enlace al siguiente empleado
                if actual_empleado.siguiente:
                    dot.edge(actual_empleado.nombre, actual_empleado.siguiente.nombre)

                # Enlace al empleado anterior (si existe)
                if actual_empleado.anterior:
                    dot.edge(actual_empleado.nombre, actual_empleado.anterior.nombre, constraint='false')

                actual_empleado = actual_empleado.siguiente

            actual_empresa = actual_empresa.siguiente
            if actual_empresa == self.primera_empresa:
                break

        dot.render(ruta_grafico, view=True)

    def contar_empresas(self):
        if not self.primera_empresa:
            return 0

        contador = 1
        actual_empresa = self.primera_empresa
        while actual_empresa.siguiente != self.primera_empresa:
            contador += 1
            actual_empresa = actual_empresa.siguiente
        return contador

    def contar_empleados_total(self):
        total = 0
        actual_empresa = self.primera_empresa
        while True:
            actual_empleado = actual_empresa.empleados_primero
            while actual_empleado:
                total += 1
                actual_empleado = actual_empleado.siguiente
            actual_empresa = actual_empresa.siguiente
            if actual_empresa == self.primera_empresa:
                break
        return total

# Función para "pretty print" de XML con indentación
def prettify_xml(element):
    rough_string = ET.tostring(element, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

# Método para guardar el XML con formato legible
def guardar_xml_formateado(lista_empresas, ruta_xml):
    root = ET.Element('empresas')
    actual_empresa = lista_empresas.primera_empresa
    while True:
        empresa_element = ET.SubElement(root, 'empresa')
        nombre_element = ET.SubElement(empresa_element, 'nombre')
        nombre_element.text = actual_empresa.nombre

        empleados_element = ET.SubElement(empresa_element, 'empleados')
        actual_empleado = actual_empresa.empleados_primero
        while actual_empleado:
            empleado_element = ET.SubElement(empleados_element, 'empleado')
            nombre_empleado_element = ET.SubElement(empleado_element, 'nombre')
            nombre_empleado_element.text = actual_empleado.nombre
            puesto_element = ET.SubElement(empleado_element, 'puesto')
            puesto_element.text = actual_empleado.puesto
            sueldo_element = ET.SubElement(empleado_element, 'sueldo')
            sueldo_element.text = actual_empleado.sueldo
            actual_empleado = actual_empleado.siguiente

        actual_empresa = actual_empresa.siguiente
        if actual_empresa == lista_empresas.primera_empresa:
            break

    # Guardar el XML con formato bonito
    xml_string = prettify_xml(root)
    with open(ruta_xml, "w", encoding="utf-8") as f:
        f.write(xml_string)
    print(f"XML guardado correctamente en {ruta_xml}")

# Código principal
if __name__ == "__main__":
    lista_empresas = ListaCircularEmpresas()

    # Solicitar la ruta del archivo XML desde consola
    ruta_xml = input("Ingrese la ruta del archivo XML para cargar las empresas y empleados: ")
    lista_empresas.cargar_desde_xml(ruta_xml)

    # Guardar el XML con formato legible
    ruta_guardado = input("Ingrese la ruta para guardar el archivo XML: ")
    guardar_xml_formateado(lista_empresas, ruta_guardado)

    # Generar el gráfico de las empresas y empleados
    ruta_grafico = input("Ingrese la ruta para guardar el gráfico: ")
    lista_empresas.generar_grafico(ruta_grafico)
