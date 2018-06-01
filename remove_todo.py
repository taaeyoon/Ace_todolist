import sqlite3
import search


def remove_todo():
    conn = sqlite3.connect("ace.db")
    cur = conn.cursor()

    loop = 'y'

    while loop == 'y' or loop == 'Y':

        # 검색코드
        search.search()

        sel_id = input("Record id? ")
        while not sel_id.isdigit():
            sel_id = input("Record id? ")
        sql = "delete from todo where id = ?"
        cur.execute(sql, (sel_id, ))

        # 제거된 항목 뒤의 id를 앞으로 1씩 당기기
        cur.execute("update todo set id = id-1 where id > ?", (sel_id))
        conn.commit()

        loop = input("\nanything else you want to remove?/n yes:y no:n ")

    conn.close()
