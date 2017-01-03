import os
import json
from models import *

env = os.environ.get
DECK_ID = env("DECK_ID")
COLLECTION_ID = env("COLLECTION_ID")
FIELDS = map(int, env("FIELDS").split(','))


def list_decks():
    reserved_names = ['Default', 'Custom study session']
    c = Collection.get(Collection.id == COLLECTION_ID)
    decks = [(d.get("id"), d.get("name"))
        for i, d in c.decks.iteritems()
        if d.get("name") not in reserved_names
    ]

    return list(sorted(decks))


def get_nid(nid):
    return Note.get(Note.id == nid)

def random_cards(n=50):
    cards = Card.select()\
        .where(
            (Card.did == DECK_ID) &
            (Card.type > 0) &
            (Card.queue > 0)
        )\
        .order_by(fn.Random())\
        .limit(n)

    for card in cards:
        note = get_nid(card.nid)
        r = []
        for f in FIELDS:
            r.append(note.flds[f])
        yield r
