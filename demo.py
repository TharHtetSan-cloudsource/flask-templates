from threading import Condition
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('demo.html')

@app.route('/form-handler', methods=['POST'])
def form():
    project_name = request.form['project_name']
    search_content = request.form['search_content']
    condition = request.form['search_options']

    output = f'Project Name: {project_name}<br>Search Content: {search_content}<br>Condition: {condition}'

    if condition == 'keyword':
        pass
    elif condition == 'domain':
        pass

    return output

app.run(host='0.0.0.0')