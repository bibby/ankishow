Passively review Anki items as a slideshow.

Build

    docker build -t ankishow .

Run

    docker run -d \
    -e DECK_ID=1482469949230 \
    -e ANKI_DB=/data/collection.anki2 \
    -e FIELDS=1,2,3 \
    -v /home/bibby/Documents/Anki/bibby:/data:ro \
    -p 8000:8000 \
    ankishow`
