from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    num1=float(request.form['num1'])
    num2=float(request.form['num2'])
    operation = request.form['operation']

    result=None
    error=None

    if operation=='add':
        result=num1+num2
    elif operation=='sub':
        result=num1-num2
    elif operation=='mul':
        result=num1 * num2
    elif operation=='div':
        try:
            result = num1/num2
        except ZeroDivisionError:
            error="Error: Cannot divide by zero"
    else:
        error="Invalid operation"

    if error is not None:
        return render_template('index.html', error=error)
    else:
        return render_template('result.html', result=result, num1=num1, num2=num2, operation=operation)

if __name__ =='__main__':
    app.run(debug=True)