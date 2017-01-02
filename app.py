import json
from flask import Flask, request, Response, render_template
from ankishow import random_cards

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.tpl')


@app.route("/data")
def data_feed():
    return Response(
        response=json.dumps([c for c in random_cards()]),
        status=200,
        mimetype="application/json"
    )
    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
