from flask import Flask, render_template, request, jsonify, redirect, url_for, session, flash
from gpt4all import GPT4All
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(32)

_model = None

users_db = {}

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


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")



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