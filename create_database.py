import sqlite3

conn = sqlite3.connect('printers.db')
cursor = conn.cursor()
cursor.execute("Create table  printers (id INTEGER PRIMARY KEY AUTOINCREMENT,"
               "model TEXT,"
               "cartridge_model TEXT,"
               "ip_address TEXT,"
               "location TEXT)")

