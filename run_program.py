import sqlite3
import list_todo
import edit
import create_db
import add_todo

#프로그램 실행코드
def run_program():
    # 개행을 위한 print()
    print()
    
    while 1:
        select = input("Choose what to do:\n(a: add data, l : List todo, m: Modify todo, q: Quit)? ")

        # 개행을 위한 print()
        print()
        
        if (select == 'a'):
            add_todo.add_todo()
        elif (select == 'l'):
            list_todo.list_todo()
        elif (select == 'm'):
            edit.edit()
        elif (select == 'q'):
            break

if __name__ == "__main__" :
    create_db.create_db()
    run_program()