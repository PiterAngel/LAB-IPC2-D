
from flask import Flask, request, render_template
import os # OBTENER POR MEDIO DEL SISTEMA
import xml.etree.ElementTree as ET

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

@app.route('/', methods=['GET', 'POST'])
def index():
    name1, age1, city1 = "", "", ""
    name2, age2, city2 = "", "", ""

    if request.method == "POST":
        file = request.files.get("file")
        if file and file.filename.endswith(".xml"):
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)

            # PROCESRAR EL ARCHIVO XML
            tree = ET.parse(file_path)
            root = tree.getroot()

            # EXTRAER LA INFORMACIÓN DE LOS REGISTROS EN EL XML
            if len(root) > 0:
                record1 = root[0]
                name1 = record1.find("name").text
                age1 = record1.find("age").text
                city1 = record1.find("city").text

            if len(root) > 1:
                record2 = root[1]
                name2 = record2.find("name").text
                age2 = record2.find("age").text
                city2 = record2.find("city").text

    # paras las variables a la plantilla
    return render_template("index.html", name1=name1, age1=age1, city1=city1, name2=name2,age2=age2, city2=city2)

if __name__ == "__main__":
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)