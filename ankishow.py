import json
from models import *


DECK_ID = '1482469949230'
COLLECTION_ID = 1
FIELDS = [1, 2, 3]


def list_decks():
    reserved_names = ['Default', 'Custom study session']
    c = Collection.get(Collection.id == COLLECTION_ID)
    decks = [(d.get("id"), d.get("name"))
        for i, d in c.decks.iteritems()
        if d.get("name") not in reserved_names
    ]
    print list(sorted(decks))


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
