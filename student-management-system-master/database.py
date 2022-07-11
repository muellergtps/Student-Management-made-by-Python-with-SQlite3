import sqlite3

kont = sqlite3.connect('local/data_get.db')
apa = kont.cursor()
apa.execute('CREATE TABLE IF NOT EXISTS \
    student (nama TEXT,kelas TEXT,sekolah TEXT,kota TEXT,provinsi TEXT)')
apa.close()