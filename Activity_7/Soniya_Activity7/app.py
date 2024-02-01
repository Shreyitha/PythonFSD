from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def calculate_result(num1, num2, operation):
    try:
        num1 = float(num1)
        num2 = float(num2)

        if operation == 'add':
            result = num1 + num2
            op_symbol = '+'
        elif operation == 'subtract':
            result = num1 - num2
            op_symbol = '-'
        elif operation == 'multiply':
            result = num1 * num2
            op_symbol = 'x'
        elif operation == 'divide':
            if num2 == 0:
                raise ValueError("Cannot divide by zero")
            result = num1 / num2
            op_symbol = '/'

        return result, op_symbol
    except ValueError as e:
        return str(e), None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = request.form['num1']
    num2 = request.form['num2']
    operation = request.form['operation']

    result, op_symbol = calculate_result(num1, num2, operation)

    return render_template('result.html', num1=num1, num2=num2, operation=op_symbol, result=result)

if __name__ == '__main__':
    app.run(debug=True)