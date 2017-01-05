Passively review Anki items as a slideshow. This is made for myself,
but publishing in case someone finds it useful.

Build

    docker build -t ankishow .

EnvVars

    COLLECTION_ID - numeric collection id, usually 1
    DECK_ID - numeric deck id. See below about obtaining it
    ANKI_DB - container path of the anki sqlite db
    FIELDS - comma separated string of card-field indexes. Helps to know your cards.
Run

    docker run -d \
    -e DECK_ID=1482469949230 \
    -e ANKI_DB=/data/collection.anki2 \
    -e FIELDS=1,2,3 \
    -v /home/bibby/Documents/Anki/bibby:/data:ro \
    -p 8000:8000 \
    ankishow`


If you don't know the DeckId for what you're trying to review, that's ok;
Assuming the Collection is id 1, you can start it without a deck and load
the path `http://localhost:8000/decks`. Record the DeckId and restart the
container.
