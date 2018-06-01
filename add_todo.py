import sqlite3
import now_date


# 항목 추가 함수
def add_todo():
    conn = sqlite3.connect("ace.db")
    cur = conn.cursor()
    place_default = ' '
    comment_default = ' '
    title = input("Todo ? ")
    print()
    due = input("Due date? (yyyy-mm-dd or mm-dd or dd)")
    print()
    # 년도 또는 달 생략 시 현재 년도와 달로 대체
    if len(due) < 10:
        due = now_date.convert_due(due)
    category = input("Category ? ")
    print()
    priority = input("Priority ? (1 to 5) ")
    print()
    while (priority != '1') and (priority != '2') and (priority != '3') and (priority != '4') and (priority != '5'):
        priority = input("Priority ? (1 to 5) ")
        print()
    edit_place = input("Want to add Place ? (y / n) ")
    print()
    if (edit_place == 'y') or (edit_place == 'Y'):
        place = input("Place ? ")
        print()
    else:
        place = place_default
    edit_comment = input("Want to add Comment ? (y / n) ")
    print()
    if (edit_comment == 'y') or (edit_comment == 'Y'):
        comment = input("Comment ? ")
        print()
    else :
        comment = comment_default
    data = ((title, category, priority, due, place, comment), )
    sql = "insert into todo (title, category, priority, due, place, comment, finished) values (?, ?, ?, ?, ?, ?,0);"
    cur.executemany(sql, data)

    conn.commit()
    conn.close()
    # 개행을 위한 print()
