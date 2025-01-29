from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)

@app.route('/index')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
