import list_todo
import edit_todo
import create_db
import add_todo
import remove_todo
import stat_todo
import search
import detail
import argparse


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
    parser = argparse.ArgumentParser()
    
    parser.add_argument("--add",help ="add item",action="store_true")
    parser.add_argument("--list",help="print list of items",action="store_true")
    parser.add_argument("--edit",help ="edit item",action="store_true")
    parser.add_argument("--stat",help ="stats of items",action="store_true")
    parser.add_argument("--search",help ="search item that you want to find",action="store_true")
    parser.add_argument("--detail",help ="print details of items that you want to see",action="store_true")
    parser.add_argument("--remove",help ="remove item that you want to remove",action="store_true")
    parser.add_argument("--version",action="version", version ="version 1.0")

    args = parser.parse_args()

    if(args.add):
        add_todo.add_todo()
    elif(args.list):
        select2 = input("Choose what to print:\n(a: all, f: finished/unfinished)? ")
        # 초기 데이터베이스 출력
        if select2 == 'a':
            select2 = 1
            list_todo.list_all()
        elif select2 == 'f':
            select2 = 2
            list_todo.list_finished_unfinished()
        status = 0
        while 1:
            option = input("Sort in other way or quit this section:\n"
                            "(t: title, c: category, o: order, d: due, q: quit)? ")
            if option == 'q':
                break
            option = OPTIONS.index(option) + 1
            # 옵션에 따른 정렬 및 출력 함수
            status = sort(int(option), status, int(select2)-1)

    elif(args.edit):
        edit_todo.edit_todo()
    elif(args.stat):
        stat_todo.stat_todo()
    elif(args.search):
        search.search()
    elif(args.detail):
        detail.detail()
    elif(args.remove):
        remove_todo.remove_todo()
    else :
        print("Hello!, This is ACE TODO APPLICATION")
        print("If you want to run action of ACE, confirm options(-h or --help)")
        print()

if __name__ == "__main__":
    create_db.create_db()
    run_program()