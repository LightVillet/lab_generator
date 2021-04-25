from os import path
import json

from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return send_from_directory(app.root.path, 'Kormen-T-Algoritmy-postroenie-i-analiz-3-e-izdanie.djvu')


if __name__ == '__main__':
    app.run(port='1337', debug=True)

