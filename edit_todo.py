import sqlite3
import list_todo
import search


def edit_todo():
    conn = sqlite3.connect("ace.db")
    cur = conn.cursor()

    loop = 'y'

    # 반복에 대해 yes라고 응답하면 반복
    while loop == 'y' or loop == 'Y':

        # 검색코드
        search.search()

        # 변경할 항목 선택
        sel_id = input("Record id? ")
        select = input(
            "What do you want to edit? \n\n Title => title"
            "\n Due date => due \n Finished => fin"
            "\n priority => priority \n category = > category"
            "\n place = > place \n comment = > comment\n")

    # 변경내용 작성
        # 타이틀 변경
        if 'title' in select:
            sel_title = input("\nTitle?")
            cur.execute("update todo set title = ? where id =?", (sel_title, sel_id))

        # 기한 변경
        elif 'due' in select:
            sel_due = input("\nDue date? ")
            cur.execute("update todo set due = ? where id =?", (sel_due, sel_id))

        # 중요도 변경
        elif 'priority' in select:
            sel_priority = input("\nPriority? ")
            cur.execute("update todo set priority = ? where id =?", (sel_priority, sel_id))

        # 완료/미완료 변경
        elif 'fin' in select:
            sel_finished = input("\nFinished (1: yes, 0: no)? ")
            cur.execute("update todo set finished = ? where id =?", (sel_finished, sel_id))

        # 카테고리 변경
        elif 'category' in select:
            sel_category = input("\nCategory? ")
            cur.execute("update todo set category = ? where id =?", (sel_category, sel_id))

        # 장소 변경
        elif 'place' in select:
            sel_place = input("\nPlace? ")
            cur.execute("update todo set place = ? where id =?", (sel_place, sel_id))

        # 세부사항 변경
        elif 'comment' in select:
            sel_comment = input("\nComment? ")
            cur.execute("update todo set comment = ? where id =?", (sel_comment, sel_id))

        conn.commit()

        loop = input("\nanything else you want to edit?/n yes:y no:n ")

    # 변경된 리스트 출력
    list_todo.list_all()
    conn.close()
