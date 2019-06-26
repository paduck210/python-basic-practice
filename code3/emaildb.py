#import Library
import sqlite3

#connect to Library
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

#if there is existing table,delete it / in case of none table, this code do notihg
cur.execute('DROP TABLE IF EXISTS Counts')

#Create New table
cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]

# ? 는 sql에서 자리표기, 뒤의 것에 의해 대체
#Not read/put data, just make cusor() ready
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))
#Grab first thing
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (email, count)
                VALUES (?, 1)''', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
                    (email,))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
