import os
from flask import (
    Flask,
    render_template
)


app = Flask(__name__)
DEBUG = os.getenv('DEBUG')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    print("ok")
    pass

if __name__ == '__main__':
    app.run(debug=DEBUG)