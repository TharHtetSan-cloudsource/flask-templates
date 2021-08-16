from flask import Flask, request, render_template,send_file
from urllib.request import urlopen

#from pyvirtualdisplay import Display
#display = Display(visible=0, size=(800, 800))  
#display.start()


app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('home.html')


@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    page_url = str(text).strip()
    output_str = "Hello : "+page_url
    return output_str



app.run(host='0.0.0.0')