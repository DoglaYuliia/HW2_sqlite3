import sqlite3
db = sqlite3.connect('example.sqlite')



cur = db.cursor()


cur. execute('''
CREATE TABLE emails (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT NOT NULL
    )
''')

cur.executescript('''
INSERT INTO emails (name, phone) VALUES ('John Din', '+380735248564');
INSERT INTO emails (name, phone) VALUES ('Kate Li', '+380965264521');
INSERT INTO emails (name, phone) VALUES ('Nick Woo', '+380662584521');
''')

db.commit()


db.close()