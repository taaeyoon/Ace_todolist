import sqlite3

def add_todo(table):
    conn = sqlite3.connect(table)

    cur = conn.cursor()

    t = input("Todo? ")
    d = input("Due date? ")
    data = ((t, d), )
    sql = "insert into todo (what, due, finished) values (?, ?, 0);"

    cur.executemany(sql, data)
    conn.commit()

    conn.close()
