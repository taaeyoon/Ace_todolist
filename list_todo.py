def list_todo():
    import sqlite3 

    conn = sqlite3.connect("ace.db")
    cur = conn.cursor()

    sql = "select * from todo where 1"
    cur.execute(sql)

    rows = cur.fetchall()
    for row in rows :
        print(str(row[0]) + " " + row[1] + " " + row[2] + " " + str(row[3]))

    # 개행을 위한 print
    print()