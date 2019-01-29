import sqlite3

conn = sqlite3.connect('Databases/orgdb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('CREATE TABLE Counts(org TEXT, count INTEGER)')

fname = input('Enter file name: ')
if len(fname) < 1 : fname = 'mbox-short.txt'

fh = open(fname)
for line in fh:
    if not line.startswith('From: '):
        continue
    
    email = line.split()[1]
    org = email.split('@')[1]

    cur.execute('Select count from Counts where org = ? ',(org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('Insert into Counts (org, count) values (?,1)',(org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',(org,))
    
conn.commit()

sqlstr = 'Select org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()