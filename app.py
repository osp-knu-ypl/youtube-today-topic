from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/method/', methods=['GET', 'POST'])
def method():
    return "method"

@app.errorhandler(404)
def page_not_found(error):
    return "페이지가 없습니다. URL을 확인하세요", 404

if __name__ == '__main__':
    app.run(debug=True)