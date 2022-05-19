from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/method/', methods=['GET', 'POST'])
def method():
    return "method"

@app.route('/apple/', methods=['GET', 'POST'])
def apple():
    return render_template('/Phone/apple.html')

@app.route('/samsung/', methods=['GET', 'POST'])
def samsung():
    return render_template('/Phone/samsung.html')

@app.route('/tablet/', methods=['GET', 'POST'])
def tablet():
    return render_template('/Phone/tablet.html')

@app.route('/cpu/', methods=['GET', 'POST'])
def cpu():
    return render_template('/PC/cpu.html')

@app.route('/gpu/', methods=['GET', 'POST'])
def gpu():
    return render_template('/PC/gpu.html')

@app.route('/ssd/', methods=['GET', 'POST'])
def ssd():
    return render_template('/PC/ssd.html')

@app.route('/tv/', methods=['GET', 'POST'])
def tv():
    return render_template('/ETC/tv.html')

@app.route('/watch/', methods=['GET', 'POST'])
def watch():
    return render_template('/ETC/watch.html')

@app.route('/console/', methods=['GET', 'POST'])
def console():
    return render_template('/ETC/console.html')

@app.route('/creators/', methods=['GET', 'POST'])
def creators():
    return render_template('/creators.html')

@app.errorhandler(404)
def page_not_found(error):
    return "페이지가 없습니다. URL을 확인하세요", 404



if __name__ == '__main__':
    app.run(debug=True)