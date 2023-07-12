from flask import Flask, request, render_template

app = Flask(__name__)
tasks = []

@app.route('/', methods=['GET', 'POST'])
def todo():
    if request.method == 'POST':
        task = request.form['task']
        tasks.append(task)
    return render_template('todo.html', tasks=tasks)

if __name__ == '__main__':
    app.run()
