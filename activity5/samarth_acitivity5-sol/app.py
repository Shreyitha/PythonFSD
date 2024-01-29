# Import the Flask module and other modules
from flask import Flask, render_template, request, redirect, url_for, flash, session
from datetime import timedelta

# Create an instance of the Flask class
app = Flask(__name__)

# Set a secret key for the session
app.secret_key = "secret"

# Set the session lifetime
app.permanent_session_lifetime = timedelta(minutes=5)

# Define a route for the login page
@app.route("/")
def login():
    # Check if the user is already logged in
    if "user" in session:
        # Redirect the user to the dashboard page
        return redirect(url_for("dashboard"))
    # Render the login.html template
    return render_template("login.html")

# Define a route for the login check
@app.route("/login", methods=["POST"])
def login_check():
    # Get the username and password from the form
    username = request.form["username"]
    password = request.form["password"]
    if username == "admin" and password == "admin":
        
        session.permanent = True
        session["user"] = username
        flash("Login successful")
        return redirect(url_for("dashboard"))
    flash("Invalid credentials")
    return redirect(url_for("login"))


@app.route("/dashboard")
def dashboard():
 
    if "user" in session:
        user = session["user"]
        return render_template("dashboard.html", user=user)
    return redirect(url_for("login"))

@app.route("/logout")
def logout():
    if "user" in session:
        session.pop("user", None)
        flash("You have been logged out")
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
