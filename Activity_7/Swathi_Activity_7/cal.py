from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        # Get user inputs from the form
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']

        # Perform the selected arithmetic operation
        if operation == 'add':
            result = num1 + num2
            operation_name = 'Addition'
        elif operation == 'subtract':
            result = num1 - num2
            operation_name = 'Subtraction'
        elif operation == 'multiply':
            result = num1 * num2
            operation_name = 'Multiplication'
        elif operation == 'divide':
            # Check for division by zero
            if num2 == 0:
                raise ValueError("Cannot divide by zero")
            result = num1 / num2
            operation_name = 'Division'
        else:
            raise ValueError("Invalid operation")

        return render_template('result.html', num1=num1, num2=num2, operation_name=operation_name, result=result)

    except ValueError as e:
        return render_template('error.html', message=str(e))

if __name__ == '__main__':
    app.run(debug=True)
