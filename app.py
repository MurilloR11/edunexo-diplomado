from flask import Flask, render_template, request, jsonify, redirect, url_for, session, flash, send_from_directory
from gpt4all import GPT4All
from sqlalchemy.exc import IntegrityError
from werkzeug.security import check_password_hash, generate_password_hash
from extensions import db, migrate

app = Flask(__name__)
app.config.from_object("config.Config")

db.init_app(app)
migrate.init_app(app, db)

from models.user import User  # noqa: E402, F401

_model = None

SYSTEM_PROMPT = (
    "Eres un asistente virtual de la plataforma educativa Edunexo. "
    "Solo respondes en español, de forma breve (máximo 2 o 3 oraciones). "
    "No saludes ni te presentes al inicio. Simplemente responde la pregunta del usuario "
    "sin generar preguntas adicionales ni ejemplos de conversación."
)

def get_model():
    global _model
    if _model is None:
        _model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf")
    return _model


def generate_response(message, max_tokens=256):
    model = get_model()
    with model.chat_session(system_prompt=SYSTEM_PROMPT):
        response = model.generate(message, max_tokens=max_tokens)
    return response


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        app.static_folder,
        "adunexo.logo.svg",
        mimetype="image/svg+xml",
    )


@app.route("/login", methods=["GET", "POST"])
def login():
    if "user_id" in session:
        return redirect(url_for("dashboard"))

    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        remember = request.form.get("remember") == "on"

        if not email or not password:
            flash("Ingresa correo y contraseña.", "error")
            return redirect(url_for("login"))

        user = User.query.filter_by(email=email).first()

        if not user or not check_password_hash(user.password_hash, password):
            flash("Credenciales incorrectas.", "error")
            return redirect(url_for("login"))

        if not user.is_active:
            flash("La cuenta está inactiva.", "error")
            return redirect(url_for("login"))

        session.clear()
        session["user_id"] = user.id
        session["user_name"] = user.full_name
        session["user_role"] = user.role
        session.permanent = remember
        flash("Inicio de sesión exitoso.", "success")
        return redirect(url_for("dashboard"))

    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if "user_id" in session:
        return redirect(url_for("dashboard"))

    if request.method == "POST":
        full_name = request.form.get("fullName", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        confirm_password = request.form.get("confirmPassword", "")
        role = request.form.get("role", "")

        valid_roles = {"DOCENTE", "ESTUDIANTE", "ADMINISTRADOR"}

        if not full_name or not email or not password or not confirm_password or not role:
            flash("Completa todos los campos obligatorios.", "error")
            return redirect(url_for("register"))

        if role not in valid_roles:
            flash("Selecciona un rol válido.", "error")
            return redirect(url_for("register"))

        if len(password) < 8:
            flash("La contraseña debe tener mínimo 8 caracteres.", "error")
            return redirect(url_for("register"))

        if password != confirm_password:
            flash("Las contraseñas no coinciden.", "error")
            return redirect(url_for("register"))

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash("Ya existe una cuenta con ese correo.", "error")
            return redirect(url_for("register"))

        user = User(
            full_name=full_name,
            email=email,
            password_hash=generate_password_hash(password),
            role=role,
        )
        db.session.add(user)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            flash("Ya existe una cuenta con ese correo.", "error")
            return redirect(url_for("register"))

        flash("Cuenta creada correctamente. Inicia sesión.", "success")
        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        flash("Inicia sesión para acceder al dashboard.", "error")
        return redirect(url_for("login"))

    return render_template(
        "dashboard.html",
        user_name=session.get("user_name"),
        user_role=session.get("user_role"),
    )


@app.route("/logout")
def logout():
    session.clear()
    flash("Sesión cerrada correctamente.", "success")
    return redirect(url_for("login"))



@app.route("/AI")
@app.route("/ai")
@app.route("/chat")
def chat_view():
    return render_template("chat.html")


@app.route("/api/chat", methods=["POST"])
def chat_api():
    data = request.get_json()
    message = data.get("message", "")
    if not message:
        return jsonify({"error": "Mensaje vacio"}), 400
    try:
        response = generate_response(message)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
