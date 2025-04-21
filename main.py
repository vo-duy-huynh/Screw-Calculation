from flask import Flask, render_template, jsonify
import json

app = Flask(__name__, template_folder='./templates', static_folder='./static')


@app.route('/')
def index():
    return render_template('./index.html')
@app.route('/tab1')
def tab1():
    # Đọc dữ liệu JSON
    with open('data02.json', 'r', encoding='utf-8') as f:
        materials = json.load(f)
    with open('hesodanbac.json', 'r', encoding='utf-8') as f:
        hesodanbacdata = json.load(f)
    return render_template('./tab1.html', materials=materials, hesodanbacdata=hesodanbacdata)
if __name__ == '__main__':
    app.run(debug=True)
