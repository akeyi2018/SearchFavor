from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def index():

    return render_template('main.html')

@app.route('/regist')
def regist():

    return render_template('regist.html')


@app.route('/view')
def view():
    return render_template('view.html')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')


