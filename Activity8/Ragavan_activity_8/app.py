from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = [
    {'content': 'Complete homework', 'complete': False},
    {'content': 'Read a book', 'complete': False},
    {'content': 'Dance', 'complete': False}
]

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task_content = request.form['task']
    tasks.append({'content': task_content, 'complete': False})
    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    tasks[task_id]['complete'] = True
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    del tasks[task_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
