
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Backend funcionando correctamente 🚀"

@app.route('/tendencias', methods=['GET'])
def get_tendencias():
    data = {"negocios": ["E-commerce de nicho", "Cursos online", "Vending Machines saludables"]}
    return jsonify(data)

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=True)


