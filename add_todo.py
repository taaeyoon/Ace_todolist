import sqlite3

def add_todo():
    conn = sqlite3.connect("ace.db")

    cur = conn.cursor()
    placedefualt = ' '
    commentdefualt = ' '
    title = input("Todo ? ")
    due = input("Due date ? ")
    categ = input("Category ? ")
    pnum = input("Order ? (1 to 5)")
    while  (pnum  != '1') and (pnum  != '2') and (pnum  != '3') and (pnum  != '4') and (pnum  != '5') :
        pnum = input("Order ? (1 to 5)")
    placeyn = input("Edit Place ? (y / n) ")
    if (placeyn == 'y') or (placeyn == 'Y') :
        place = input("Place ? ")
    else :
        place = placedefualt
    commentyn = input("Edit Comment ? (y / n) ")
    if (commentyn == 'y') or (commentyn == 'Y') :
        comment = input("Comment ? ")
    else :
        comment = commentdefualt
    data = ((title, due, categ, pnum, place, comment), )
    sql = "insert into todo (what, due, categ, pnum, place, comment, finished) values (?, ?, ?, ?, ?, ?,0);"

    cur.executemany(sql, data)
    conn.commit()

    conn.close()

    # 개행을 위한 print()
    print()
