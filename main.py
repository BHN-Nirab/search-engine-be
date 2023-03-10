from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def root():
    data = {
        'message': 'Hello, world!'
    }
    return jsonify(data)


@app.route('/api/<parameter>')
def api(parameter):
    response = {"message": "Hello, {}".format(parameter)}
    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, ssl_context=('adhoc'))
