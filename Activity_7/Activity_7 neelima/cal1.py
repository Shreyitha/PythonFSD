from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def calculate_result(num1, num2, operation):
    try:
        num1 = float(num1)
        num2 = float(num2)

        if operation == 'addition':
            result = num1 + num2
            operator = '+'
        elif operation == 'subtraction':
            result = num1 - num2
            operator = '-'
        elif operation == 'multiplication':
            result = num1 * num2
            operator = '*'
        elif operation == 'division':
            if num2 == 0:
                return None, None, None  # Division by zero error
            result = num1 / num2
            operator = '/'
        else:
            return None, None, None  # Invalid operation

        return result, operator, None

    except ValueError:
        return None, None, 'Invalid input'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = request.form['num1']
    operation = request.form['operation']
    num2 = request.form['num2']

    result, operator, error = calculate_result(num1, num2, operation)

    if error:
        return render_template('error.html', error=error)

    return render_template('result.html', num1=num1, num2=num2, operator=operator, result=result)

if __name__ == '__main__':
    app.run(debug=True)
