from flask import Flask
import os

app = Flask(__name__)
app.static_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
app.template_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')

from app import routes
