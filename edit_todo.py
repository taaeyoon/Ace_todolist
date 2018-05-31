import sqlite3
import list_todo


def edit():
    conn = sqlite3.connect("ace.db")
    cur = conn.cursor()

    # 수정 전 리스트로 보여주기
    list_todo.list_all()

    # 변경할 리스트항목의 넘버
    id_number = input("Record id ? ")

    # 변경할 카테고리 선택
    what_to_do = input("What do you want to edit? \n title => TITLE\n "
                       "Due date => DUE\n Category => CAT\n Order => ORDER\n "
                       "Finished => FIN\n : ")

    # 변경내용 작성
    if 'TODO' in what_to_do:
        todo = input("Todo ? ")
        sql = "UPDATE todo SET title=? WHERE id=?"
        data = (
            (todo, id_number),
        )
        cur.executemany(sql, data)

    if 'DUE' in what_to_do:
        due = input("Due date ? ")
        sql = "UPDATE todo SET due=? WHERE id=?"
        data = (
            (due, id_number),
        )
        cur.executemany(sql, data)

    if 'CAT' in what_to_do:
        cat = input("Category? ")
        sql = "UPDATE todo SET category=? WHERE id=?"
        data = (
            (cat, id_number),
        )
        cur.excutemany(sql, data)

    if 'ORDER' in what_to_do:
        order = input("Order? ")
        sql = "UPDATE todo SET priority=? WHERE id=?"
        data = (
            (order, id_number),
        )
        cur.executemany(sql, data)

    if 'FIN' in what_to_do:
        fin = input("Finished (1: yes, 0: no)? ")
        sql = "UPDATE todo SET finished=? WHERE id=?"
        data = (
            (fin, id_number),
        )
        cur.executemany(sql, data)

    conn.commit()
    # 변경된 리스트 출력
    list_todo.list_all()
    conn.close()
