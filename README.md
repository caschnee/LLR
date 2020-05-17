# LLR (Language Learning Ressources)

## Anki 
### Add Kanji Study reference ID to Anki flashcards (Japanese Learning & Anki Mobile App)

When reviewing a japanese word on the Anki mobile App, open the Kanji Study page for the sepcific word by clicking on a link. This to quickly review details and meaning of the specific Kanji(s).

You need the following before running the script:

* ANKI_PATH: Complete path to Anki source code. e.g. '/home/User/Documents/LLR/anki'. To get the source code, run the command below:

```
git clone https://github.com/ankitects/anki
cd anki
git checkout tags/2.1.15
```

* COLLECTION_PATH: Path to the Anki collection, e.g. /home/USER/.local/share/Anki2/USER/collection.anki2
* KANJISTUDY_PATH: Extract Kanji Study database from the apk in assets/content.db/content.db (or download it [here](https://drive.google.com/file/d/1XA8Pv3lEMtGB1OC9zS7qyi7UuGXC_duf/view?usp=sharing))
* NOTE_TYPE: Anki Note type you want to add the reference to Kanji Study to
* ANKI_FIELD_KANJI_STUDY_REF: The field in NOTE_TYPE to contain the reference to Kanji Study. e.g. 'reference_kanji_study'. You must create the field in Anki BEFORE running the script. The field should be empty
* ANKI_FIELD_WORD_JAPANESE: The field in NOTE_TYPE that contains the japanese word to lookup in Kanji Study. e.g. 'word_japanese'

Close Anki and run the script. Use absolute path. Consider making a copy of the Anki collection before running the script.
```
python3 add_kanji_study_reference.py -A ANKI_PATH -C COLLECTION_PATH -K KANJISTUDY_PATH -N NOTE_TYPE -F KANJI_STUDY_ANKI_FIELD -W ANKI_FIELD_WORD_JAPANESE
```

For example:

```
python3 add_kanji_study_reference.py -A '/home/<User>/Documents/LLR/anki' -C '/home/<User>/.local/share/Anki2/<User>/collection.anki2' -K '/home/<User>/Documents/LLR/content.db' -N 'Japanese_Voc' -F 'reference_kanji_study' -W 'word_japanese'
```

Then, update your card template in Anki to add the link to Kanji Study, for example:

```
<a href="kanjistudy://word?id={{reference_kanji_study}}">{{word_japanese}}</a>
```

You should be able to access the specific Kanji in Kanji Study app (if you have it on your phone) by clicking on the link in the Anki Application. Tested with Android.
