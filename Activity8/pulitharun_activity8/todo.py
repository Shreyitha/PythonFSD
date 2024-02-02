from flask import *

app = Flask(__name__)

todo = []

@app.route('/')
def home():
    return render_template('index.html', todo=todo)

@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    todo.append(task)
    return redirect(url_for('home'))

@app.route('/complete/<int:id>')
def complete(id):
    todo[id] = '<strike>' + todo[id] + '</strike>'
    return redirect(url_for('home'))

@app.route('/delete/<int:id>')
def delete(id):
    del todo[id]
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
