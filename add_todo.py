import sqlite3
import now_date


# 항목 추가 함수
def add_todo():
    conn = sqlite3.connect("ace.db")
    cur = conn.cursor()
    placedefault = ' '
    commentdefault = ' '
    title = input("Todo ? ")
    due = input("Due date? (yyyy-mm-dd or mm-dd or dd)")
    # 년도 또는 달 생략 시 현재 년도와 달로 대체
    if len(due) < 10:
        due = now_date.convert_due(due)

    category = input("Category ? ")
    priority = input("Order ? (1 to 5)")
    while  (priority  != '1') and (priority  != '2') and (priority  != '3') and (priority  != '4') and (priority  != '5') :
        priority = input("Order ? (1 to 5)")
    placeyn = input("Edit Place ? (y / n) ")
    if (placeyn == 'y') or (placeyn == 'Y') :
        place = input("Place ? ")
    else :
        place = placedefault
    commentyn = input("Edit Comment ? (y / n) ")
    if (commentyn == 'y') or (commentyn == 'Y') :
        comment = input("Comment ? ")
    else :
        comment = commentdefualt
    data = ((title, due, categ, pnum, place, comment), )
    sql = "insert into todo (title, due, categ, pnum, place, comment, finished) values (?, ?, ?, ?, ?, ?,0);"
        comment = commentdefault
    data = ((title, due, category, priority, place, comment), )
    sql = "insert into todo (what, due, category, priority, place, comment, finished) values (?, ?, ?, ?, ?, ?,0);"


    cur.executemany(sql, data)

    conn.commit()
    conn.close()
    # 개행을 위한 print()
    print()
