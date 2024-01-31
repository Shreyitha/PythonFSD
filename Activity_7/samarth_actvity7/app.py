from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')



@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = request.form['num1']
    num2 = request.form['num2']
    operation = request.form['operation']
    if not num1.isdigit() or not num2.isdigit():
        return 'Invalid input. Please enter numbers only.'
    if operation == 'add':
        result = int(num1) + int(num2)
        operator = '+'
    elif operation == 'subtract':
        result = int(num1) - int(num2)
        operator = '-'
    elif operation == 'multiply':
        result = int(num1) * int(num2)
        operator = '*'
    elif operation == 'divide':
        if num2 == '0':
            return 'Cannot divide by zero.'
        result = int(num1) / int(num2)
        operator = '/'
    return render_template('result.html', num1=num1, num2=num2, operator=operator, result=result)

if __name__ == '__main__':
    app.run(debug=True)
