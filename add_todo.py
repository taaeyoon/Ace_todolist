import sqlite3
import now_date


# 항목 추가 함수
def add_todo():
    conn = sqlite3.connect("ace.db")
    cur = conn.cursor()
    place_default = ' '
    comment_default = ' '
    title = input("Todo ? ")
    due = input("Due date? (yyyy-mm-dd or mm-dd or dd)")
    # 년도 또는 달 생략 시 현재 년도와 달로 대체
    if len(due) < 10:
        due = now_date.convert_due(due)
    category = input("Category ? ")
    priority = input("Priority ? (1 to 5)")
    while (priority != '1') and (priority != '2') and (priority != '3') and (priority != '4') and (priority != '5'):
        priority = input("Priority ? (1 to 5)")

    edit_place = input("Edit Place ? (y / n) ")
    if (edit_place == 'y') or (edit_place == 'Y'):
        place = input("Place ? ")
    else:
        place = place_default
    edit_comment = input("Edit Comment ? (y / n) ")
    if (edit_comment == 'y') or (edit_comment == 'Y'):
        comment = input("Comment ? ")
    else :
        comment = commentdefault
    data = ((title, category, priority, due, place, comment), )
    sql = "insert into todo (title, category, priority, due, place, comment, finished) values (?, ?, ?, ?, ?, ?,0);"
    cur.executemany(sql, data)

    conn.commit()
    conn.close()
    # 개행을 위한 print()
    print()
