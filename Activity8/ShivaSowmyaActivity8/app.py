from flask import Flask,render_template,url_for,request,redirect
app=Flask(__name__)
task_list=[]

@app.route("/")
def home():
    return render_template("index.html",task_list=task_list)

@app.route("/add_task",methods=["POST"])
def add_task():
    task=request.form["newtask"]
    task_list.append({"data":task,"status":"incomplete"})
    return redirect(url_for("home"))


@app.route("/delete/<int:index>")
def delete_task(index):
    del task_list[index]
    return redirect(url_for("home"))

@app.route("/complete/<int:index>")
def complete_task(index):
    task_list[index]["status"]="complete"
    return redirect(url_for("home"))


if __name__=='__main__':
    app.run(debug=True)