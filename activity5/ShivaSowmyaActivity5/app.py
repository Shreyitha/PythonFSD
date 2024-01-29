from flask import Flask,redirect,render_template,request,url_for,flash,session,redirect
import logging
app=Flask(__name__)
app.secret_key = 'mysecretkey'

@app.route("/")
def login():
    return render_template("login.html")


@app.route("/checklogin" , methods=["post"])
def check_login():
    username= request.form.get("username")
    password=request.form.get("password")
    if username=="admin" and password=="admin":
        flash('Login successful')
        session['logged_in_user']='admin'
        return redirect(url_for('dashboard'))
    else:
        return render_template("login.html",error=True)
    
@app.route("/dashboard")
def dashboard():
        if 'logged_in_user' in session and session['logged_in_user']:
             username = session['logged_in_user']
        else:
            return redirect(url_for("login"))

        return render_template('dashboard.html',username=username)


@app.route("/logout")
def logout():
    flash('you have been logged out')
    session.pop('logged_in_user',None)
    return redirect(url_for('login'))
 


if __name__=="__main__":
    app.run(debug=True)