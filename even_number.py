from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/even_numbers', methods=['POST'])
def generate_even_numbers():
    n = int(request.form.get('n', 0))
    numbers = [2 * i for i in range(1, n+1)]
    return json.dumps(numbers)

if __name__ == '__even_number__':
    app.run(host='127.0.0.1', port=8080, debug=True)
