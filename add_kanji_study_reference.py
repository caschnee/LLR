import sys
import sqlite3
import argparse

# Path to Anki source code, download here https://github.com/ankitects/anki
ANKI_PATH='./anki'

# Path to the Anki collection, e.g. /home/<USER>/.local/share/Anki2/<USER>/collection.anki2
COLLECTION_PATH='/home/<USER>/.local/share/Anki2/<USER>/collection.anki2'

# Extract Kanji Study database assets/content.db/content.db an place it in the current directory
KANJI_STUDY_PATH='./content.db'

# Anki Note type to add kanji study reference to
NOTE_TYPE='Japanese'

# The field in NOTE_TYPE to contain the reference to Kanji Study
ANKI_FIELD_KANJI_STUDY_REF='reference_kanji_study'

# The field in NOTE_TYPE that contain the japanese word to lookup in Kanji Study
ANKI_FIELD_WORD_JAPANESE='word_japanese'

def get_kanji_study(kanji_study_path, col, note_type, anki_field_kanji_study, anki_field_word_japanese):
    note_ids = col.findCards("(note:" + note_type + ") card:1 " + anki_field_kanji_study + ": ")
    con = sqlite3.connect(kanji_study_path)
    c = con.cursor()
    for note_id in note_ids:
        note = col.getCard(note_id).note()
        t = (note[anki_field_word_japanese],)
        print("Search Kanji Study database for word " + str(note[anki_field_word_japanese]))
        try:
            c.execute('SELECT * FROM vocab WHERE entry=?', t)
            res = c.fetchone()
            if res:
                print("Kanji Study reference found for word: " + str(note[anki_field_word_japanese]))
                note.__setitem__(anki_field_kanji_study, str(res[0]))
                note.flush()
            else:
                c.execute('SELECT * FROM vocab WHERE entry LIKE "%'+ note[anki_field_word_japanese] + '%"')
                res = c.fetchone()
                if res:
                    print("Kanji Study reference found for word" + str(note[anki_field_word_japanese]))
                    note.__setitem__(anki_field_kanji_study, str(res[0]))
                    note.flush()
        except Exception as e:
            print("ERROR SQL execution")
            print(e)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-A", "--anki", type=str, help="Path to anki source code")
    parser.add_argument("-C", "--collection", type=str, help="Path to the anki collection you want to modify")
    parser.add_argument("-K", "--KanjiDB", type=str, help="Path to Kanji Study database")
    parser.add_argument("-N", "--noteType", type=str, help="Anki Note type you want to modify")
    parser.add_argument("-F", "--field", type=str, help="The field name that will contain the reference to Kanji Study")
    parser.add_argument("-W", "--fieldWord", type=str, help="The field in NOTE_TYPE that contain the japanese word to lookup in Kanji Study")

    args = parser.parse_args()

    if args.anki:
        ANKI_PATH = args.anki
    if args.collection:
        COLLECTION_PATH = args.collection
    if args.KanjiDB:
        KANJI_STUDY_PATH = args.KanjiDB
    if args.noteType:
        NOTE_TYPE = args.noteType
    if args.field:
        ANKI_FIELD_KANJI_STUDY_REF = args.field
    if args.fieldWord:
        ANKI_FIELD_WORD_JAPANESE = args.fieldWord

    print(ANKI_PATH)

    # Append Anki path to import anki
    sys.path.append(ANKI_PATH)
    from anki import Collection

    col = Collection(COLLECTION_PATH)

    try:
        get_kanji_study(KANJI_STUDY_PATH,
                        col,
                        NOTE_TYPE,
                        ANKI_FIELD_KANJI_STUDY_REF,
                        ANKI_FIELD_WORD_JAPANESE)
    except Exception as e:
        print(e)

    col.close()
