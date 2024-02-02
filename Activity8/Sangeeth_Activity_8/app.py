from flask import Flask, render_template, request, redirect, url_for

app= Flask(__name__)

todos= []

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    todo= request.form.get('todo')
    todos.append({'task':todo, 'done': False})
    return redirect(url_for('index'))

@app.route('/edit/<int:index>',methods=['GET', 'POST'])
def edit(index):
    todo= todos[index]
    if request.method=='POST':
        todo['task']= request.form.get('todo')
        return redirect(url_for('index'))
    else:
        return render_template("edit.html", index=index, todo=todo)
    
@app.route('/check/<int:index>')
def check(index):
    todos[index]['done']= not todos[index]['done']
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete(index):
    del todos[index]
    return redirect(url_for('index'))

if __name__=='__main__':
    app.run(debug=True)
