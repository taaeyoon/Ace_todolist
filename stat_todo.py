import sqlite3
from datetime import datetime

NOW = datetime.now()


def stat_todo():
    conn = sqlite3.connect("ace.db")
    cur = conn.cursor()
    finished_number = 0
    yet_number = 0
    list_all_number = 0
    category_number = 0
    due_over_number = 0

    sql = "select * from todo where 1"
    cur.execute(sql)
    rows = cur.fetchall()
    conn.close()

    for row in rows:
        category_number = len(row)
        list_all_number = list_all_number + 1
        if row[7] == 1:
            finished_number = finished_number + 1
        else:
            yet_number = yet_number + 1
            if int(row[4][:4]) < int(NOW.year):
                due_over_number = due_over_number + 1
            else:
                if row[4][5] == '0':
                    if int(row[4][6]) < int(NOW.month):
                        due_over_number = due_over_number + 1
                else:
                    if int(row[4][5:7]) < int(NOW.month):
                        due_over_number = due_over_number + 1
                    else:
                        if int(row[4][8:10]) < int(NOW.day):
                            due_over_number = due_over_number + 1
                        else:
                            due_over_number = due_over_number

    print("percentage of finished list : " + str(round((finished_number/list_all_number)*100, 2)))
    print("percentage of finished list : " + str(round((yet_number/list_all_number)*100, 2)))
    print("number of lists : " + str(list_all_number))
    print("number of categories : " + str(category_number))
    print("number of overdue lists : " + str(due_over_number))
