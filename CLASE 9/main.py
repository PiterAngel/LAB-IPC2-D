from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

class User:
    name = None
    email = None
    password = None

    @classmethod
    def register(cls, name, email, password):
        cls.name = name
        cls.email = email
        cls.password = password

    @classmethod
    def verify(cls, email, password):
        return cls.email == email and cls.password == password

@app.route("/")
def index():
    return render_template("register.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register", methods=["POST"])
def register():
    try:
        if request.is_json:
            data = request.get_json()
        else:
            data = request.form.to_dict()

        if not data:
            return jsonify({"error": "Datos no proporcionados"}), 400

        name = data.get("name")
        email = data.get("email")
        password = data.get("password")

        if not name or not email or not password:
            return jsonify({"error": "Campo(s) faltante(s)"}), 400

        User.register(name, email, password)
        print(f"Registrado: Nombre: {name} - Email: {email}")

        # Redirigir a la página de inicio de sesión después de un registro exitoso
        return redirect(url_for("login"))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/login", methods=["POST"])
def submit_login():
    try:
        if request.is_json:
            data = request.get_json()
        else:
            data = request.form.to_dict()

        if not data:
            return jsonify({"error": "Datos no proporcionados"}), 400

        email = data.get("email")
        password = data.get("password")

        if not email or not password:
            return jsonify({"error": "Campo(s) faltante(s)"}), 400

        if User.verify(email, password):
            User.name = User.name  # Asegúrate de asignar el nombre al usuario actual
            print(f"Login exitoso: {User.name}")
            # Redirigir al dashboard después de un inicio de sesión exitoso
            return redirect(url_for("dashboard"))
        else:
            print("Credenciales incorrectas")
            return jsonify({"error": "Credenciales incorrectas"}), 401
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/dashboard")
def dashboard():
    if User.name:
        return render_template("dashboard.html", User=User)
    else:
        return jsonify({"error": "No autenticado"}), 401

if __name__ == "__main__":
    app.run(debug=True)
