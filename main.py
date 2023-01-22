from flask import Flask, request, render_template
import pandas as pd
import os
app = Flask(__name__)
app.config['uploads'] = './uploads'


@app.route('/')
def index():
    return render_template('main.html')

@app.route('/regist')
def regist():
    return render_template('regist.html')


@app.route('/view_csv', methods=['GET','POST'])
def view():
    if request.method == 'POST':
        # 表示行数の取得
        view_row = request.form['rows']
        # ファイル名取得
        data_stream = request.files['send_data']
        file_name = data_stream.filename
        full_path = os.path.join(app.config['uploads'], file_name)
        # ファイルを保存する
        data_stream.save(full_path)
        # 読み込み
        df = pd.read_csv(full_path,encoding='utf-8')
        headers = df.columns.to_list()
        res = df.sample(int(view_row)).to_numpy().tolist()
        ct = len(res)
        return render_template('main.html', result=res, headers = headers, ct=ct)
    return ''

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')


