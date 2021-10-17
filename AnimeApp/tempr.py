import os
import sys
import requests


response=requests.get("https://animechan.vercel.app/api/random").json()

L=[]
for i in response.values():
    L.append(i)

print(L)

import sqlite3

conn=sqlite3.connect("Anime_backend.db")
c=conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS mytable(Anime TEXT,Character TEXT, Quote TEXT)')

def data_entry():
    c.execute("INSERT INTO mytable(Anime, Character,Quote) values(?,?,?)",(L[0],L[1],L[2],))
    conn.commit()
    conn.close()

create_table()
data_entry()



 