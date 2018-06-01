import sqlite3
from datetime import datetime

def stat_todo() :
    conn = sqlite3.connect("ace.db")
    cur = conn.cursor()

    NOW = datetime.now()
    categorylist = ['']
    finishednumber = 0
    yetnumber = 0
    listallnumber = 0
    categorynumber = 0
    dueovernumber = 0
    i = 0

    sql = "select * from todo where 1"
    cur.execute(sql)
    rows = cur.fetchall()
    conn.close()

    for row in rows:
        listallnumber = listallnumber + 1
        if row[2] not in categorylist[i] :
            categorylist.append(row[2])
        if row[7] == 1 :
            finishednumber = finishednumber + 1
        else :
            yetnumber = yetnumber + 1
            if int(row[4][:4]) < int(NOW.year) :
                dueovernumber = dueovernumber + 1
            else :
                if row[4][5] == '0' :
                    if int(row[4][6]) < int(NOW.month) :
                        dueovernumber = dueovernumber + 1
                else :
                    if int(row[4][5:7]) < int(NOW.month) :
                        dueovernumber = dueovernumber + 1
                    else :
                        if int(row[4][8:10]) < int(NOW.day) :
                            dueovernumber = dueovernumber + 1
                        else :
                            dueovernumber = dueovernumber
    categorynumber = len(categorylist) - 1

    print("percentage of finished list : " + str(round((finishednumber/listallnumber)*100, 2)) + "% ")
    print()
    print("percentage of unfinished list : " + str(round((yetnumber/listallnumber)*100, 2)) + "% ")
    print()
    print("number of lists : " + str(listallnumber))
    print()
    print("number of categories : " + str(categorynumber))
    print()
    print("number of overdue lists : " + str(dueovernumber))
    print()
