
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/tendencias', methods=['GET'])
def get_tendencias():
    data = {"negocios": ["E-commerce de nicho", "Cursos online", "Vending Machines saludables"]}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
