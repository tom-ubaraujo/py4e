import xml.etree.ElementTree as ET 
import sqlite3

# create the connection with the db
conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

# make new tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id INTEGER,
    title TEXT UNIQUE
);

CREATE TABLE Track(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id INTEGER,
    genre_id INTEGER,
    len INTEGER,
    rating INTEGER,
    count INTEGER
);
''')

fname = input('Enter file name: ')
if (len(fname) <1 ):
    fname = 'Library_assign.xml'

def lookup(d, key):
    found = False
    for child in d:
        if found:
            return child.text 
        if child.tag == 'key' and child.text == key:
            found = True
    return None

# parse the xml via ElementTree
stuff = ET.parse(fname)

# find all the third level dicts, which is every song.
# each element is a song's dict
all = stuff.findall('dict/dict/dict')
print('Dict count: ', len(all))

for song in all:
    if (lookup(song, 'Track ID') is None):
        continue

    name = lookup(song, 'Name')
    artist = lookup(song, 'Artist')
    album = lookup(song, 'Album')
    count = lookup(song, 'Play Count')
    rating = lookup(song, 'Rating')
    length = lookup(song, 'Total Time')
    genre = lookup(song, 'Genre')

    if name is None or artist is None or album is None or genre is None:
        continue
    
    print(name, artist, album, count, rating, length)

    cur.execute('''INSERT OR IGNORE INTO Artist(name)
        VALUES (?)''',(artist,))
    cur.execute('SELECT id FROM Artist WHERE name = ?', (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Genre(name)
        VALUES (?)''',(genre,))
    cur.execute('SELECT id FROM Genre WHERE name = ?', (genre, ))
    genre_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )''', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count) 
        VALUES ( ?, ?, ?, ?, ?, ? )''', 
        ( name, album_id, genre_id, length, rating, count ) )

    conn.commit()
