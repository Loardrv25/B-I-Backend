import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilitar CORS para permitir acceso desde el frontend

# Función para hacer scraping de Shopify
def obtener_ideas_negocio():
    URL = "https://www.shopify.com/blog/most-profitable-businesses"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(URL, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        ideas = [idea.text.strip() for idea in soup.find_all("h2")]
        return ideas  # Enviamos todas las ideas sin filtrar
    else:
        return ["❌ Error al obtener ideas"]

@app.route('/')
def home():
    return "Backend funcionando correctamente 🚀"

@app.route('/tendencias', methods=['GET'])
def get_tendencias():
    ideas = obtener_ideas_negocio()
    return jsonify({"negocios": ideas})

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=True)
