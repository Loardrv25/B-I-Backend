from flask import Flask, jsonify
from flask_cors import CORS  # Importar CORS

app = Flask(__name__)
CORS(app)  # Habilitar CORS en toda la aplicación

@app.route('/')
def home():
    return "Backend funcionando correctamente 🚀"

@app.route('/tendencias', methods=['GET'])
def get_tendencias():
    data = {
        "negocios": [
            "E-commerce de nicho",
            "Cursos online",
            "Vending Machines saludables"
        ]
    }
    return jsonify(data)

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 10000))  # Render usa este puerto
    app.run(host="0.0.0.0", port=port, debug=True)
