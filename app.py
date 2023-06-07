from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    csv_file = request.files['file']
    
    df = pd.read_csv(csv_file, delimiter=';')
    
    
    return render_template('display.html', data=df.to_html())

if __name__ == '__main__':
    app.run(debug=True)