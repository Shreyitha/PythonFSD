from flask import Flask,render_template,flash,request,redirect,url_for
app = Flask(__name__)
app.secret_key = "todolistkey"

def displaylist():
    global availabletasklist,completedtasklist
    completedtasklist = []
    availabletasklist = ["Practice Coding","Read a book","Watch Movies","Play Games"]
    return availabletasklist,completedtasklist

displaylist()
@app.route("/")
def index():
    return render_template("todo.html",availabletasklist=availabletasklist,completedtasklist=completedtasklist)

def addtasks(inp):
    global availabletasklist,completedtasklist
    if inp not in availabletasklist:
        availabletasklist.append(inp)
    else:
        flash(inp+" task already exists!")
    return availabletasklist,completedtasklist

def deletetask(inp):
    global availabletasklist,completedtasklist
    if inp in availabletasklist:
        availabletasklist.remove(inp)
    elif inp in completedtasklist:
        completedtasklist.remove(inp)
    else:
        flash(inp+" is not yet added to delete")
    return availabletasklist,completedtasklist

def markcompleted(inp):
    global availabletasklist,completedtasklist
    if inp not in completedtasklist and inp in availabletasklist:
        completedtasklist.append(inp)
    if inp in availabletasklist:
        availabletasklist.remove(inp)
    elif inp not in availabletasklist and inp not in completedtasklist:
        flash(inp+" is not yet added to mark as complete")
    else:
        flash(inp+" already marked as completed")
    return availabletasklist,completedtasklist

@app.route("/todolist",methods=["post"])
def todolist():
    top = request.form.get("TOP")
    inp = str(request.form.get("TASK"))
    if top == "add":
        addtasks(inp)
        return redirect(url_for("index"))
    elif top == "delete":
        deletetask(inp)
        return redirect(url_for("index"))
    else:
        markcompleted(inp)
        return redirect(url_for("index"))

if __name__=='__main__':
    app.run(debug=True)