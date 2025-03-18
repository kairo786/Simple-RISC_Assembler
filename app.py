from flask import Flask, request, jsonify, send_from_directory
from assembler import Assembler, opcodes

app = Flask(__name__)

@app.route('/assemble', methods=['POST'])
def assemble():
    try:
        if not request.is_json:
            return jsonify({"success": False, "error": "Request must be JSON"}), 400
            
        data = request.json
        if 'code' not in data:
            return jsonify({"success": False, "error": "Missing 'code' field in request"}), 400
            
        asm = Assembler()
        src = data['code']
        machine_code = asm.assemble(src)
        
        return jsonify({
            "success": True,
            "output": [format(c, '04x') for c in machine_code],
            "binary": [format(c, '016b') for c in machine_code],
            "count": len(machine_code)
        })
    except Exception as e:
        return jsonify({"success": False, "error": f"Assembly Error: {str(e)}"}), 400

@app.route('/opcodes', methods=['GET'])
def get_opcodes():
    return jsonify({
        "success": True,
        "opcodes": {k: format(v, '05b') for k, v in opcodes.items()}
    })

@app.route('/', methods=['GET'])
def index():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)