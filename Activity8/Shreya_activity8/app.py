from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


tasks=[]
task_id = 1


@app.route('/')
def home():
    return render_template('index.html', tasks=tasks)


@app.route('/add', methods=['POST'])
def add_task():
    global task_id
    content = request.form['content']
    tasks.append({"id": task_id, "content": content, "completed": False})
    task_id += 1
    return redirect(url_for('home'))


@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            break
    return redirect(url_for('home'))


@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
