from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulação de licenças (pode ser substituído por JSON/DB futuramente)
licencas = {
    "admita": "ativo",
    "benedetti": "inativo",
    "salomon": "inativo",
    "alvaz": "inativo"
}

@app.route('/')
def home():
    return "API de Licenciamento ativa."

@app.route('/verificar_licenca', methods=['GET'])
def verificar_licenca():
    cliente = request.args.get('cliente')
    status = licencas.get(cliente, "inativo")
    return jsonify({"status": status})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
