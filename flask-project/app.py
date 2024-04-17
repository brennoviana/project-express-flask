from flask import Flask, render_template
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__, template_folder='app/templates')

@app.route('/movies')
def login():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=os.getenv('PORT'), debug=True)
