from flask import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/calculate', methods = ['POST'])
def calculator():
    try:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']
        
        if operation == 'add':
            result = num1+num2
            operation_str = 'addition'
        elif operation == "sub":
            result = num1-num2
            operation_str = 'subtraction'
        elif operation == "mul":
            result = num1*num2
            operation_str = 'multificaton'
        elif operation == "div":
            if num2 == 0:
                raise  ValueError("Cannot divide by zero!")
            else:
                result = num1/num2
                operation_str = 'Division'
        else:
            return "Invalid Operation "
        
        return  render_template('result.html', num1 = num1, num2 = num2, result= result,  operation = operation_str)
    
    except ValueError as ve:
        return render_template("error.html", error = ve)

if  __name__=='__main__':
    app.run(debug=True)

    
