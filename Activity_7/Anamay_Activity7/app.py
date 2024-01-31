from flask import Flask, render_template, request, redirect, url_for, flash
'''
Written By - Anamay Dubey
Date - 31/01/24
Title - Activity 7 
'''
app = Flask(__name__)
app.secret_key = 'anamay_secret_key'
def calculate_result(num1, num2, operation):
    try:
        num1 = float(num1)
        num2 = float(num2)
        if operation == 'addition':
            result = num1 + num2
            operation_symbol = '+'
        elif operation == 'subtraction':
            result = num1 - num2
            operation_symbol = '-'
        elif operation == 'multiplication':
            result = num1 * num2
            operation_symbol = '×'
        elif operation == 'division':
            if num2 == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            result = num1 / num2
            operation_symbol = '÷'
        else:
            return None, None, None, 'Error: Invalid operation!'
        return num1, num2, result, operation_symbol, None
    except ValueError:
        return None, None, None, 'Error: Invalid input! Please enter numeric values.'
    except ZeroDivisionError:
        return None, None, None, 'Error: Division by zero!'
    except Exception as e:
        return None, None, None, f'Error: {str(e)}'

@app.route('/', methods=['GET', 'POST'])
def calculator():
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        operation = request.form['operation']
        num1, num2, result, operation_symbol, error = calculate_result(num1, num2, operation)
        if error:
            flash(error, 'error')
        else:
            flash('Calculation successful!', 'success')
            return redirect(url_for('result', num1=num1, num2=num2, result=result, operation_symbol=operation_symbol, error=error))
    return render_template('index.html')

@app.route('/result')
def result():
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')
    result = request.args.get('result')
    operation_symbol = request.args.get('operation_symbol')
    error = request.args.get('error')
    return render_template('result.html', num1=num1, num2=num2, result=result, operation_symbol=operation_symbol, error=error)

if __name__ == '__main__':
    app.run(debug=True)
