from flask import Flask
from sklearn.externals import joblib


app = Flask(__name__)
app.config.from_object("app.config")

# unpickle my model

from .views import *

# Handle Bad Requests
@app.errorhandler(404)
def page_not_found(e):
    """Page Not Found"""
    return render_template('404.html'), 404
