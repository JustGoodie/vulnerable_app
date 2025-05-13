from flask import Flask, request

app = Flask(__name__)

@app.route('/greet')
def greet():
    name = request.args.get('name')
    return f'Hello, {name}'  # Уязвимость: XSS

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)