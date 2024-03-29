import os
from os.path import isfile
import sqlite3


con = sqlite3.connect("db.sqlite3", check_same_thread=False)
cur = con.cursor()



def insert_request(request):
    sql = f"""INSERT INTO requests (date, text, size_x, size_y, fps, length) VALUES (?, ?, ?, ?, ?, ? )""" 
    cur.execute(sql, request)
    pass

def sql_main(request):
    try:
        cur.execute("SELECT text FROM requests")
    except Exception:
        cur.execute("""CREATE TABLE requests (
            ID integer NOT NULL PRIMARY KEY AUTOINCREMENT,
            date datetime NOT NULL,
            text text,
            size_x integer,
            size_y integer,
            fps integer,
            length integer
            )""")
    insert_request(request)
    con.commit()

if __name__ == "__main__":
    request = ("1.10", "sample_text", 100, 100, 20, 3)
    sql_main(request)


