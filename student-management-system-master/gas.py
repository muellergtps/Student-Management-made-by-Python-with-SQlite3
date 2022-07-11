import os
from posixpath import split
from secrets import choice
import sqlite3

# STudent-Management-Project By Ryve X Imanroem
kont = sqlite3.connect('local/data_get.db')
apa = kont.cursor()

def view_data():
    xc = 0
    data = apa.execute('SELECT * FROM student')
    print("--->Data Para Pelajar<---") # Student Management 
    print('------------------------\n')
    for vc in data.fetchall():
        xc += 1
        print("NO.")
        print(str(xc),vc) # print(str(xc), vc[0] , vc[1] , vc[2] , vc[3])  ~  without Array
    print('-----------------------------\n')

def insert_cok():
    view_data()
    nama = input("Nama mu : ") #  name = input("Yourname : ")
    kelas = input("Kelas mu : ") # grade/class = input("Yourgrade : ")
    sekolah = input("Asal Sekolah : ") # school = input("Your School : ")
    kota = input("Asal Kota/Askot : ") # City/Town = input("City where you live : ")
    provinsi = input("Provinsi : ") # province = input("Province : ")
    data_terkumpul = [nama,kelas,sekolah,kota,provinsi] # ah anj semua codinger handal bisa googling sendiri lah anj jan manja
    apa.execute('INSERT INTO student (nama,kelas,sekolah,kota,provinsi) VALUES (?,?,?,?,?)', data_terkumpul)
    kont.commit()
    print('\n')

def delete_data():
    view_data()
    print("~Tulis nama sesuai Uppercase dan Lowercase untuk menghapus DATA~")
    hapus_data = input("Hapus datamu : ")
    data_hapus = [hapus_data]
    apa.execute('delete from student where nama = ?', data_hapus)
    kont.commit()
    print('\n')
    
# os.system('clear') for Linux/ OS X 
os.system('cls') # For Windows 
loop = True
while (loop):
    print("Welcome to Student Management!")
    print("0. Keluar")
    print("1. Insert data")
    print("2. Remove data")
    print("3. View data\n")
    choice = int(input("Opsi> "))
    # os.system('clear') for Linux/ OS X
    os.system('cls') # for windows
    if(choice == 0):
        loop = False
    elif(choice == 1):
        insert_cok()
    elif(choice == 2):
        delete_data()
    elif(choice == 3):
        view_data()

# Pesan Moral : Mending Turu 😅👆 ~~~ Indonesia
# Moral Expression : Better sleep 😅👆 ~~~ English

# Ryve X Imanroem | Project Newbie ~~~ English
# Ryve X Imanroem | Projek Pemula ~~~ Indonesia 

# This file has finish Monday , 11 July 2022 08:46pm ~~~ English
# File ini selesai dibuat Senin , 11 Juli 2022 08:46pm ~~~ Indonesia
 #                           ¥
# Other Language you can open Google translate :) ~~~ English
# Bahasa lainnya kamu bisa cari di Google penerjemah :) ~~~ Indonesia