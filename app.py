from flask import Flask, render_template, request, jsonify
from packages.calculator import Calculator
from packages.mongodb import initialize_database, end_session_update, store_history, dump_data_to_file, collection
import json

app = Flask(__name__)

@app.route('/')
def index():
    initialize_database()  # Initialize the database if necessary
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    number1 = request.form.get('number1', type=float)
    number2 = request.form.get('number2', type=float)
    operation = request.form.get('operation')

    calculator = Calculator()
    calculator.set_values(number1, number2, operation)
    result = calculator.calculate()

    # Store calculation history
    store_history(number1, number2, operation, result)

    return render_template('index.html', result=result)

@app.route('/shutdown', methods=['POST'])
def shutdown():
    dump_data_to_file('data.json')
    shutdown_server()
    return 'Server shutting down...'

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

if __name__ == '__main__':
    app.run(debug=True)
