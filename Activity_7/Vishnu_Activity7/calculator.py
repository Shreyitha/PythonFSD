from flask import Flask,render_template,flash,request,redirect,url_for
app = Flask(__name__)
app.secret_key = "flaskcalculator"

@app.route("/")
def home():
    return render_template("home.html")

def verifyinputs(num1,num2,operator):
        if (num1!="") and (num2!="") and (operator!=""):
            isok = "okay"
            if num1.isalpha() or num2.isalpha():
                isok = "notokay"
            elif float(num1) and float(num2):
                isok = "okay"
            return isok

@app.route("/calculator",methods=["post"])
def calculator():
    num1 = request.form.get("NUM1")
    num2 = request.form.get("NUM2")
    operator = request.form.get("OPERATOR")
    result = 0
    if verifyinputs(num1,num2,operator) == "okay":
        num1 = float(num1)
        num2 = float(num2)
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1*num2
        elif operator == "/":
            try:
                result = num1/num2
            except ZeroDivisionError:
                flash("Zero cannot be used as number for division!")
                return redirect(url_for("home"))
    
        return render_template("calculatorresult.html",num1=num1,num2=num2,operator=operator,result=result)
    elif verifyinputs(num1,num2,operator) == "notokay":
        flash("Inputs must be numbers only!!")
        return redirect(url_for("home"))
    else:
        flash("Inputs cannot be empty!!")
        return redirect(url_for("home"))

if __name__=='__main__':
    app.run(debug=True)