from django.shortcuts import render

# Create your views here.
import re

def index(request):
    entrada = ""
    salida = ""

    if request.method == 'POST':
        entrada = request.POST['entrada']
        salida = analizar_xml(entrada)

    return render(request, 'analyzer/index.html', {'entrada': entrada, 'salida': salida})

def analizar_xml(xml_texto):
    # Contar ventas por departamento usando regex
    ventas_departamentos = {}
    pattern = r'<Venta departamento="([^"]+)">.*?<Fecha>(.*?)<\/Fecha>'

    matches = re.findall(pattern, xml_texto, re.DOTALL)
    
    for match in matches:
        departamento, fecha = match
        if departamento in ventas_departamentos:
            ventas_departamentos[departamento] += 1
        else:
            ventas_departamentos[departamento] = 1

    # Generar el XML de salida
    xml_salida = '<?xml version="1.0" encoding="UTF-8"?>\n<resultados>\n<departamentos>\n'
    for departamento, cantidad in ventas_departamentos.items():
        xml_salida += f'<{departamento}>\n<cantidadVentas>{cantidad}</cantidadVentas>\n</{departamento}>\n'
    xml_salida += '</departamentos>\n</resultados>'

    return xml_salida
