import sqlite3
import list_todo


def edit():
    conn = sqlite3.connect("ace.db")
    cur = conn.cursor()

    # 수정 전 리스트로 보여주기
    list_todo.list_todo()
    print('\n')

    # 변경할 항목 선택
    whattodo = input("What do you want to edit? \n Record ID => ID\n Todo => TODO\n Due date => DUE\n Finished => FIN")

    #변경내용 작성
    if 'ID' in  whattodo :
        id = input("Record id ? ")
    if 'TODO' in  whattodo :
        todo = input("Todo ? ")
    if 'DUE' in  whattodo :
        due = input("Due date ? ")
    if 'FIN' in  whattodo :
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

