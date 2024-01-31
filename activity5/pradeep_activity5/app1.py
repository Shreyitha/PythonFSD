from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = "Sai_Pradeep"

@app.route('/login', methods=['GET'])
def login():
    return render_template("login.html")

@app.route('/login-submit', methods=['POST'])
def loginSubmit():
    username = request.form.get("username")
    password = request.form.get("password")

    if(username == 'admin' and password == 'admin'):
        flash("Login Successful")
        session['log_user']= username
        return redirect(url_for('dashboard'))
    else:
        
        return render_template("login.html", error = True)
        
    

@app.route("/dashboard")
def dashboard():
    
    if 'log_user' in session and session['log_user']:
        username = session['log_user']
    else:
        return redirect(url_for("login"))

    return render_template("dashboard.html", username=username)

@app.route("/logout")
def logout():
    #flash('you have been logged out')
    session.pop('log_user',None)
    return redirect(url_for('login'))

if __name__=='__main__':
    app.run(debug=True)
