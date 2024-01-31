from flask import Flask,render_template,redirect,request,url_for


app=Flask(__name__)

@app.route("/result")
def result():
    num1 = float(request.args.get("num1"))
    num2 = float(request.args.get("num2"))
    res = float(request.args.get("res"))
    op=request.args.get("op")
    return render_template("result.html",num1=num1,num2=num2,res=res,op=op)
    
@app.route("/checkdata" ,methods=["POST"])
def checkdata():
    try:
        num1 = float(request.form["num1"])
        num2 = float(request.form["num2"])
        op = request.form["op"]

        if op == '+':
            res = num1 + num2
        elif op == '-':
            res = num1 - num2
        elif op == '*':
            res = num1 * num2
        elif op == '/' and num2 != 0:
            res = num1 / num2
        else:
            return render_template("index.html", error=True)

        return redirect(url_for('result', num1=num1,num2=num2,res=res,op=op))

    except ValueError:
        return render_template("index.html", error=True)

    
@app.route("/")
def home():
    return render_template("index.html")


if __name__=='__main__':
    app.run(debug=True)