import list_todo
import edit_todo
import create_db
import add_todo
import search

COLUMN = ["title", "category", "priority", "due"]
SORT = ["asc", "desc"]
OPTIONS = ["t", "c", "o", "d"]


# 정렬 함수 (option은 정렬 대상, status는 정렬 방식(오름차/내립차순), finished는 완료 여부에 따른 출력 방식을 결정)
def sort(option, status, finished):
    if finished == 0:
        if option == status:
            list_todo.list_all(COLUMN[option-1] + " " + SORT[1])
            return 0
        else:
            list_todo.list_all(COLUMN[option-1] + " " + SORT[0])
            return option
    else:
        if option == status:
            list_todo.list_finished_unfinished(COLUMN[option-1] + " " + SORT[1])
            return 0
        else:
            list_todo.list_finished_unfinished(COLUMN[option-1] + " " + SORT[0])
            return option


# 프로그램 실행코드
def run_program():
    # 개행을 위한 print()
    print()
    while 1:
        select = input("Choose what to do:\n(a: add data, l : List todo, m: Modify todo, s: Search, q: Quit)? ")
        # 개행을 위한 print()
        print()
        if select == 'a':
            add_todo.add_todo()
        elif select == 'l':
            select2 = input("Choose what to print:\n(a: all, f: finished/unfinished)? ")
            # 초기 데이터베이스 출력
            if select2 == 'a':
                select2 = 1
                list_todo.list_all()
            elif select2 == 'f':
                select2 = 2
                list_todo.list_finished_unfinished()
            status = 0
            # 옵션 입력(기본값은 오름차순, 동일한 옵션을 입력할 시 차순 변경)
            while 1:
                option = input("Sort in other way or quit this section:\n"
                               "(t: title, c: category, o: order, d: due, q: quit)? ")
                if option == 'q':
                    break
                option = OPTIONS.index(option) + 1
                # 옵션에 따른 정렬 및 출력 함수
                status = sort(int(option), status, int(select2)-1)
        elif select == 'm':
            edit_todo.edit()

        elif select == "s":
            search.search()
            
        elif select == 'q':
            break


if __name__ == "__main__" :
    create_db.create_db()
    run_program()
