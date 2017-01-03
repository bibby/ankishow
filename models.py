import os
import json
from peewee import *

ANKI_DB = os.environ.get("ANKI_DB", 'collection.anki2')
db = SqliteDatabase(ANKI_DB)


class JSONField(Field):
    def coerce(self, value):
        if isinstance(value, dict):
            return value
        return json.loads(value)


class UnitField(Field):
    def coerce(self, value):
        if isinstance(value, list):
            return value
        return value.split(chr(0x1f))


class Collection(Model):
    #  arbitrary number since there is only one row
    id = IntegerField()

    #  created timestamp
    crt = IntegerField()

    #  last modified in milliseconds
    mod = IntegerField()

    #  schema mod time: time when "schema" was modified.
    #    If server scm is different from the client scm a full-sync is required
    scm = IntegerField()

    #  version
    ver = IntegerField()

    #  dirty: unused, set to 0
    dty = IntegerField()

    #  update sequence number: used for finding diffs when syncing.
    #    See usn in cards table for more details.
    usn = IntegerField()

    #  "last sync time"
    ls = IntegerField()

    #  json object containing configuration options that are synced
    conf = JSONField()

    #  json array of json objects containing the models (aka Note types)
    models = JSONField()

    #  json array of json objects containing the deck
    decks = JSONField()

    #  json array of json objects containing the deck options
    dconf = JSONField()

    # space separated string?
    tags = CharField()

    class Meta:
        database = db
        db_table = 'col'

class Note(Model):
    # epoch seconds of when the note was created
    id = IntegerField()

    # globally unique id, almost certainly used for syncing
    guid = CharField()

    # model id
    mid = IntegerField()

    # modification timestamp, epoch seconds
    mod = IntegerField()

    # update sequence number: for finding diffs when syncing.
    #   See the description in the cards table for more info
    usn = IntegerField()

    # space-separated string of tags.
    #   includes space at the beginning and end, for LIKE "% tag %" queries
    tags = CharField()

    # the values of the fields in this note. separated by 0x1f (31) character.
    flds = UnitField()

    # sort field: used for quick sorting and duplicate check
    sfld = CharField()

    # field checksum used for duplicate check.
    #   integer representation of first 8 digits of sha1 hash of the first field
    csum = IntegerField()

    # unused
    flags = IntegerField()

    # unused
    data = CharField()

    class Meta:
        database = db
        db_table = 'notes'

class Card(Model):
    # the epoch milliseconds of when the card was created
    id = IntegerField()

    # notes.id
    nid = IntegerField()

    # deck id (available in col table)
    did = IntegerField()

    # ordinal : identifies which of the card templates it corresponds to
    #   valid values are from 0 to num templates - 1
    ord = IntegerField()

    # modificaton time as epoch seconds
    mod = IntegerField()

    # update sequence number : used to figure out diffs when syncing.
    #   value of -1 indicates changes that need to be pushed to server.
    #   usn < server usn indicates changes that need to be pulled from server.
    usn = IntegerField()

    # 0=new, 1=learning, 2=due
    type = IntegerField()

    # Same as type, but -1=suspended, -2=user buried, -3=sched buried
    queue = IntegerField()

    # Due is used differently for different card types:
    #   new: note id or random int
    #   due: integer day, relative to the collection's creation time
    #   learning: integer timestamp
    due = IntegerField()

    # interval (used in SRS algorithm). Negative = seconds, possitive = days
    ivl = IntegerField()

    # factor (used in SRS algorithm)
    factor = IntegerField()

    # number of reviews
    reps = IntegerField()

    # the number of times the card went from a "was answered correctly"
    #   to "was answered incorrectly" state
    lapses = IntegerField()

    # reps left till graduation
    left = IntegerField()

    # original due: only used when the card is currently in filtered deck
    odue = IntegerField()

    # original did: only used when the card is currently in filtered deck
    odid = IntegerField()

    # currently unused
    flags = IntegerField()

    # currently unused
    data = CharField()

    class Meta:
        database = db
        db_table = 'cards'
