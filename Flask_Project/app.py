from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/results', methods=['POST'])
def results():
    test_string = request.form['test_string']
    pattern = request.form['pattern']

    matches = re.findall(pattern, test_string)

    return render_template('home.html', test_string=test_string, pattern=pattern, matches=matches)

@app.route('/validate_email', methods=['POST'])
def validate_email():
    email = request.form['email']
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    valid = re.match(email_regex, email) is not None

    return render_template('home.html', email=email, valid=valid)

if __name__ =='__main__':
    app.run(debug=True)


