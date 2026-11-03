from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    # host='0.0.0.0' mengizinkan website diakses dari perangkat lain (HP) dalam 1 jaringan WiFi
    app.run(host='0.0.0.0', debug=True, port=5000)