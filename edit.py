import sqlite3
import list_todo


def edit():
    conn = sqlite3.connect("ace.db")
    cur = conn.cursor()

    # 수정 전 리스트로 보여주기
    list_todo.list_todo()

    id = input("Record id ? ")
    todo = input("Todo ? ")
    due = input("Due date ? ")
    fin = input("Finished (1: yes, 0: no)? ")
    
    sql = "UPDATE todo SET what=?, due=?, finished=? WHERE id=?"
    data = (
        (todo, due, fin, id),
    )
    
    cur.executemany(sql, data)
    conn.commit()
    conn.close()

    # 개행을 위한 print
    print()