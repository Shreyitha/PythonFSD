from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []

@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)

@app.route("/add_task", methods=["POST"])
def add_task():
    if request.method == "POST":
        content = request.form["content"]
        new_task = {"id": len(tasks) + 1, "content": content, "completed": False}
        tasks.append(new_task)
    return redirect(url_for("index"))

@app.route("/complete_task/<int:task_id>")
def complete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = not task["completed"]
    return redirect(url_for("index"))

@app.route("/delete_task/<int:task_id>")
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
