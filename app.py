from flask import Flask, render_template, request, jsonify
from gpt4all import GPT4All

app = Flask(__name__)

_model = None

def get_model():
    global _model
    if _model is None:
        _model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf")
    return _model

def generate_response(message, max_tokens=256):
    model = get_model()
    prompt = (
        "Eres un asistente virtual de la plataforma educativa Edunexo. "
        "Solo respondes en español, de forma breve (maximo 2 o 3 oraciones). "
        "No saludes ni te presentes, simplemente responde la pregunta.\n\n"
        f"PREGUNTA: {message}\n"
        "RESPUESTA:"
    )
    return model.generate(prompt, max_tokens=max_tokens)


@app.route("/")
def index():
    return render_template("index.html")


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
