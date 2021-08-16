from flask import Flask, request, render_template,send_file
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time
import numpy as np
from treeTraversal import TreeTraversal
from ecommerce import isEcommerce
import os
import json
#from pyvirtualdisplay import Display
#display = Display(visible=0, size=(800, 800))  
#display.start()


app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('home.html')




app.run(host='0.0.0.0')