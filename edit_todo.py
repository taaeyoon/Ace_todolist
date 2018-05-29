import sqlite3
import list_todo


def edit():
    conn = sqlite3.connect("ace.db")
    cur = conn.cursor()

    # 수정 전 리스트로 보여주기
    list_todo.list_all()

    # 변경할 리스트항목의 넘버
    id = input("Record id ? ")

    # 변경할 카테고리 선택
    whattodo = input("What do you want to edit? \n title => TITLE\n "
                     "Due date => DUE\n Category => CAT\n Order => ORDER\n "
                     "Finished => FIN\n : ")

    # 변경내용 작성
    if 'TODO' in whattodo:
        todo = input("Todo ? ")
        sql = "UPDATE todo SET title=? WHERE id=?"
        data = (
            (todo, id),
        )
        cur.executemany(sql, data)

    if 'DUE' in whattodo:
        due = input("Due date ? ")
        sql = "UPDATE todo SET due=? WHERE id=?"
        data = (
            (due, id),
        )
        cur.executemany(sql, data)

    if 'CAT' in whattodo:
        cat = input("Category? ")
        sql = "UPDATE todo SET category=? WHERE id=?"
        data = (
            (cat, id),
        )
        cur.excutemany(sql, data)

    if 'ORDER' in whattodo:
        order = input("Order? ")
        sql = "UPDATE todo SET priority=? WHERE id=?"
        data = (
            (order, id),
        )
        cur.executemany(sql, data)

    if 'FIN' in whattodo:
        fin = input("Finished (1: yes, 0: no)? ")
        sql = "UPDATE todo SET finished=? WHERE id=?"
        data = (
            (fin, id),
        )
        cur.executemany(sql, data)

    conn.commit()
    # 변경된 리스트 출력
    list_todo.list_all()
    conn.close()
