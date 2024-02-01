from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    if request.method == 'POST':
        num1 = request.form.get('num1')
        num2 = request.form.get('num2')
        operation = request.form.get('operation')

        if not num1.isdigit() or not num2.isdigit():
            return "Invalid input. Please enter numeric values."

        num1 = int(num1)
        num2 = int(num2)

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                return "Error: Division by zero is not allowed."
            result = num1 / num2

        return render_template('result.html',result=result)

    return render_template('calculator.html')

if __name__ == '__main__':
    app.run(debug=True)
