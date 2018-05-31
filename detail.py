# 선택한 항목의 세부사항을 보여주는 함수 

import sqlite3, search

def detail() :
    
    conn = sqlite3.connect("ace.db")
    cur = conn.cursor()

    col_list = ["id","title","category","priority","due","place","comment","finished"]

    # 세부사항을 보고 싶은 항목의 id 선택하기
    detail_id = input("choose id of item that you want to see details: ")
    
    sql = "select * from todo where id=?"
    cur.execute(sql,(detail_id,))

    row = cur.fetchone()

    # 항목 보여주기
    for i in range(0,len(col_list)):
        print(col_list[i],":",row[i])

    print()

    cur.close()
    conn.close()