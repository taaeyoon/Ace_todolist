import sqlite3


def edit():
    conn = sqlite3.connect("lab.db")
    cur = conn.cursor()
    id = input("Record id ?")
    todo = input("Todo ?")
    due = input("Due date ?")
    fin = input("Finished (1: yes, 0: no)?")
    sql = "UPDATE todo SET what=?, due=?, finished=? WHERE id=?"
    data = (
        (id, todo, due, fin),
    )
    cur.executemany(sql, data)
    conn.commit()
    conn.close()
