from flask import Flask, render_template
from config import Config

app = Flask(__name__)

app.config.from_object(Config)

@app.route('/')
def pre_save():
    return render_template('pre_save.html')

if __name__ == '__main__':
    app.run(debug=True)
