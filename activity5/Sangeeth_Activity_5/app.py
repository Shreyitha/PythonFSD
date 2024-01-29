from flask import Flask, render_template,request,session,flash,redirect,url_for

app= Flask(__name__)
app.secret_key='mykey'

@app.route('/login', methods=['GET'])
def Login():
    return render_template('login.html')

@app.route('/login-submit', methods=['POST'])
def LoginSubmit():
    username= request.form.get("username")
    password= request.form.get("password")

    if username=='admin' and password=='admin':
        flash("You are logged in succesfully")
        session['login']= username
        return redirect(url_for('dashboard'))
    
    else:
        return render_template('login.html', error=True)
    
@app.route('/dashboard')
def dashboard():
    if 'login' in session and session['login']!= None:
        username= session['login']
    else:
        return redirect(url_for('login'))  

    return render_template('dashboard.html', username=username)  

@app.route('/logout')
def Logout():
    flash('You have been logged out succesfully')
    session.pop('login',None)
    return redirect(url_for('Login'))




if __name__== '__main__':
    app.run(debug=True)
