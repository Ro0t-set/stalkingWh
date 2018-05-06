import sqlite3
import os
import datetime
from acces import Acces

conn = sqlite3.connect('acces.db')


c = conn.cursor()

# c.execute("""CREATE TABLE acces(

# 			name text,
# 			state boolean,
# 			accesdate date
# 		   )""")

name= 'tomaso'
onlinedate=datetime.datetime.now().strftime("%y-%m-%d, %H:%M")

complilation=Acces(name,1,onlinedate)

c.execute("INSERT INTO acces VALUES('{}', '{}', '{}')".format(complilation.name, complilation.state, complilation.accesdate))

#c.execute("INSERT INTO acces VALUES('bella', '10')")

# c.execute("SELECT * FROM acces WHERE name='Bella' ")

conn.commit()

conn.close()