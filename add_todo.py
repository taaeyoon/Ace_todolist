import sqlite3
import now_date


# 항목 추가 함수
def add_todo():
    conn = sqlite3.connect("ace.db")
    cur = conn.cursor()

    # 각 항목의 정보 입력
    t = input("Todo? ")
    d = input("Due date? (yyyy-mm-dd or mm-dd or dd)")
    # 년도 또는 달 생략 시 현재 년도와 달로 대체
    if len(d) < 10:
        d = now_date.convert_due(d)
    c = input("Category? ")
    p = input("Order? ")

    data = ((t, d, c, p), )
    sql = "insert into todo (title, due, category, priority, finished) values (?, ?, ?, ?, 0);"
    cur.executemany(sql, data)

    conn.commit()
    conn.close()
    # 개행을 위한 print()
    print()
