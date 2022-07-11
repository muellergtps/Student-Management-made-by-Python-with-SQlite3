from posixpath import split
import sqlite3

kon = sqlite3.connect('local/data_get.db')
apa = kon.cursor()
apa.execute('SELECT * FROM student')
for row in apa.fetchall():
    print(row)
apa.close()
kon.close()