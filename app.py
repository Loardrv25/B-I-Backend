
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/tendencias', methods=['GET'])
def get_tendencias():
    data = {"negocios": ["E-commerce de nicho", "Cursos online", "Vending Machines saludables"]}
    return jsonify(data)

import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  # Render asigna el puerto automáticamente
    app.run(host="0.0.0.0", port=port, debug=True)


