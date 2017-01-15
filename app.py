import os
import json
import magic
from flask import Flask, request, Response, render_template, abort
from ankishow import random_cards, list_decks

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.tpl')


@app.route("/write/<int:num>")
def pick_page(num):
    return render_template('write.html', cards=random_cards(num))


@app.route("/data/<int:num>")
def data_feed_n(num):
    return get_cards(num)


@app.route("/data")
def data_feed():
    return get_cards()


def get_cards(num=None):
    return Response(
        response=json.dumps([c for c in random_cards(num)]),
        status=200,
        mimetype="application/json"
    )


@app.route("/decks")
def decks():
    return Response(
        response=json.dumps(list_decks()),
        status=200,
        mimetype="application/json"
    )

@app.route("/audio/<string:mp3>")
def audio(mp3):
    path = "/data/collection.media/" + mp3
    exists = os.path.isfile(path)
    if not exists:
        abort(404)

    return Response(
        response=open(path).read(),
        status=200,
        mimetype=magic.from_file(path, mime=True)
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
