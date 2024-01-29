from flask import Flask, render_template, request,redirect,url_for, session, flash

app = Flask(__name__)
app.secret_key = 'mysecretkey'

@app.route("/login", methods=["GET"])
def login():
    return render_template("login.html")

@app.route("/login-details", methods=["post"])
def logindetails():
    username = request.form.get("username")
    password = request.form.get("password")
    if username== 'admin' and password == 'admin':
        flash('Login successful')
        session['user']='admin'
        return redirect(url_for('dashboard')) 
    else:
        flash('user not found')
        return render_template("login.html", error =True)

@app.route("/dashboard")
def dashboard():
    if 'user' in session and session['user']:
        username = session['user']
        return render_template("dashboard.html", username=username)
    else:
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    flash('you have been logged out')
    session.pop('user',None)
    return redirect(url_for('login'))

if __name__=='__main__':
    app.run(debug=True)