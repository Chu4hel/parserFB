from setting import db
import sqlite3

def insertdb(where='', data1='', data2=''):
    conn = sqlite3.connect(db)
    command = conn.cursor()
    command = conn.execute("""INSERT INTO {0}({1})
            VALUES({2});""".format(where,data1,data2))
    conn.commit()