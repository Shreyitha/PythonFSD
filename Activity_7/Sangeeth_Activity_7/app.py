#venv-->calenv
from flask import Flask, redirect, request, render_template, url_for, flash

app= Flask(__name__)
app.secret_key = 'my_secret_key'

def is_valid_num(value):
    try:
        if float(value):
            return True
    except ValueError:
        return False


@app.route('/calc', methods=['GET'])
def calculator():
    return render_template('calc.html')

@app.route('/calc-submit', methods=['POST'])
def calculate():
    num1= int(request.form.get('num1'))
    num2= int(request.form.get('num2'))
    operation= request.form.get('operation')

    if is_valid_num(num1) and is_valid_num(num2):
        if operation== 'addition':
            result= num1+num2
        elif operation== 'subtraction':
            result= num1-num2
        elif operation== 'multiplication':
            result= num1*num2
        elif operation== 'division':
            try:
                result=num1/num2
            except ZeroDivisionError:
                return redirect(url_for('calculator', error=True))
        else:
            flash('Choose an operation to perform')  
            return redirect(url_for('calculator'))  

        return redirect(url_for('Result',operation=operation, num1=num1, num2=num2, result=result))

    return redirect(url_for('calculator'))     

@app.route('/result')
def Result():
    num1= request.args.get('num1')
    num2= request.args.get('num2')
    operation= request.args.get('operation')
    result= request.args.get('result')
    return render_template('result.html', operation=operation, num1=num1, num2=num2, result=result) 


if __name__=='__main__':
    app.run(debug=True)
                                
