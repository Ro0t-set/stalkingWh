
import sqlite3
import os
import datetime
from acces import Acces

conn = sqlite3.connect('acces.db')
c = conn.cursor()

def filter_name(username):
	c.execute("SELECT * FROM acces WHERE name=:name ",{'name':username})
	return(c.fetchall())

lista= filter_name('Lolli')

print(lista)


conn.commit()
conn.close()