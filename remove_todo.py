import sqlite3
import list_todo
import search


def remove_todo():
    conn = sqlite3.connect("ace.db")
    cur = conn.cursor()

    loop = 'y'

    while loop == 'y' or loop == 'Y':

        # 검색코드
        search.search()

        sel_id = input("Record id? ")
        sql = "delete from todo where id = ?"
        cur.execute(sql,(sel_id,))
        conn.commit()

        loop = input("anything else you want to remove?/n yes:y no:n ")

    conn.close()
