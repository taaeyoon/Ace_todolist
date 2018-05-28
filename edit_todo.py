import sqlite3

def edit():
    conn = sqlite3.connect("ace.db")
    cur = conn.cursor()

    # 수정 전 리스트로 보여주기
    sql =" select * from todo where 1"
    cur.execute(sql)
    rows = cur.fetchall()
    print("ID  TODO   DATE   FINISHED? \n---------------------------")
    for row in rows:
        ln = row[0]
        print(row[0],row[1],row[2],row[3])

    #변경할 리스트항목의 넘버
    id = input("Record id ? ")
    while int(id) > ln or int(id) < 1 :
        id = input("Record id ? ")

    # 변경할 카테고리 선택
    whattodo = input("What do you want to edit? \n Todo => TODO\n Due date => DUE\n Finished => FIN\n : ")

    #변경내용 작성
    if 'TODO' in  whattodo :
        todo = input("Todo ? ")
        sql = "UPDATE todo SET what=? WHERE id=?"
        data = (
            (todo, id),
        )
        cur.executemany(sql, data)

    if 'DUE' in  whattodo :
        due = input("Due date ? ")
        sql = "UPDATE todo SET due=? WHERE id=?"
        data = (
            (due, id),
        )
        cur.executemany(sql, data)

    if 'FIN' in  whattodo :
        fin = input("Finished (1: yes, 0: no)? ")
        sql = "UPDATE todo SET finished=? WHERE id=?"
        data = (
            (fin, id),
        )
        cur.executemany(sql, data)

#변경된 리스트 출력
    sql =" select * from todo where 1"
    cur.execute(sql)
    rows = cur.fetchall()
    print("ID  TODO   DATE   FINISHED? \n---------------------------")
    for row in rows:
        print(row[0],row[1],row[2],row[3])

    conn.commit()
    conn.close()
