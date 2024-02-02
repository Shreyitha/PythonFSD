from flask import *

app = Flask(__name__)

tasks = []

@app.route("/", methods = ['GET','POST'])
def home():
    if request.method == 'POST':
        task = request.form.get('new_task')
        tasks.append({'id':len(tasks)+1, 'task':task, 'completed': False})
    return render_template("index.html", tasks = tasks)

        

@app.route("/complete_task/<int:task_id>") 
def complete_task(task_id):
    task = next((t for t in tasks if t['id']==task_id),None)
    if task:
        task['completed']=not task['completed'] 
    return redirect(url_for("home"))

@app.route("/delete_task/<int:task_id>")
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t['id'] != task_id]
    return redirect(url_for("home"))

if (__name__) == '__main__':
    app.run(debug= True)


