# 선택한 항목의 세부사항을 보여주는 함수 

import sqlite3, search

def detail() :
    
    conn = sqlite3.connect("ace.db")
    cur = conn.cursor()

    # 세부사항을 보고 싶은 항목의 id 선택하기
    detail_id = input("choose id of item that you want to see details: ")
    
    sql = "select * from todo where id=?"
    cur.execute(sql,(detail_id,))

    row = cur.fetchone()

    # 항목 보여주기
    for element in row :
        print(element," ", end="")

    print()

    cur.close()
    conn.close()