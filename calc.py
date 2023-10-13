from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/sum', methods=['POST'])
def sum():
    d = request.get_json()
    a = d['a']
    b = d['b']
    res = a + b
    return jsonify({'result': res})

@app.route('/dif', methods=['POST'])
def dif():
    d = request.get_json()
    a = d['a']
    b = d['b']
    res = a - b
    return jsonify({'result': res})

@app.route('/mul', methods=['POST'])
def mul():
    d = request.get_json()
    a = d['a']
    b = d['b']
    res = a * b
    return jsonify({'result': res})

@app.route('/div', methods=['POST'])
def div():
    d = request.get_json()
    a = d['a']
    b = d['b']
    res = a / b
    if b == 0:
        return jsonify({'Учи матчасть!'})
    else:
        return jsonify({'result': res})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)