import xml.etree.ElementTree as ET
from graphviz import Digraph

# Clase Nodo
class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None

# Clase Lista Circular
class ListaCircular:
    def __init__(self):
        self.primero = None

    def agregar(self, nombre):
        nuevo_nodo = Nodo(nombre)
        if not self.primero:
            self.primero = nuevo_nodo
            self.primero.siguiente = self.primero  # Cierra la lista circular
        else:
            actual = self.primero
            while actual.siguiente != self.primero:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.siguiente = self.primero  # Mantiene la circularidad

    def existe(self, nombre):
        actual = self.primero
        if not actual:
            return False
        while True:
            if actual.nombre == nombre:
                return True
            actual = actual.siguiente
            if actual == self.primero:
                break
        return False

    def mostrar(self):
        if not self.primero:
            print("Lista vacía.")
            return
        actual = self.primero
        while True:
            print(f"Nombre: {actual.nombre}")
            actual = actual.siguiente
            if actual == self.primero:
                break

    def generar_grafico(self, ruta_grafico):
        dot = Digraph(comment='Lista Circular')
        actual = self.primero
        if not actual:
            return
        while True:
            dot.node(actual.nombre)
            dot.edge(actual.nombre, actual.siguiente.nombre)
            actual = actual.siguiente
            if actual == self.primero:
                break
        dot.render(ruta_grafico, view=True)

    def cargar_desde_xml(self, ruta_xml):
        tree = ET.parse(ruta_xml)
        root = tree.getroot()
        for elem in root.findall('nombre'):
            self.agregar(elem.text)

    def escribir_a_xml(self, ruta_xml):
        root = ET.Element("nombres")
        actual = self.primero
        if not actual:
            return
        while True:
            nombre_elem = ET.SubElement(root, "nombre")
            nombre_elem.text = actual.nombre
            actual = actual.siguiente
            if actual == self.primero:
                break
        tree = ET.ElementTree(root)
        tree.write(ruta_xml)

# Ejemplo de uso
if __name__ == "__main__":
    lista = ListaCircular()

    # Solicitar la ruta del archivo XML desde consola
    ruta_xml = input("Ingrese la ruta del archivo XML para cargar los nombres: ")
    lista.cargar_desde_xml(ruta_xml)
    lista.mostrar()

    # Verificar la existencia de un nombre
    nombre_a_buscar = input("Ingrese el nombre a buscar en la lista: ")
    if lista.existe(nombre_a_buscar):
        print(f"El nombre {nombre_a_buscar} existe en la lista.")
    else:
        print(f"El nombre {nombre_a_buscar} no existe en la lista.")

    # Generar gráfico de la lista circular
    ruta_grafico = input("Ingrese la ruta para guardar el gráfico: ")
    lista.generar_grafico(ruta_grafico)

    # Guardar la lista a un nuevo archivo XML
    ruta_xml_guardar = input("Ingrese la ruta para guardar el archivo XML actualizado: ")
    lista.escribir_a_xml(ruta_xml_guardar)
