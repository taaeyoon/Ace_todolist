import sqlite3

def create_db():

    conn = sqlite3.connect("ace.db")
    cur = conn.cursor()

    table_create_sql = """create table if not exists todo(
		id integer primary key autoincrement,
		what text not null,
		due text not null,
                category text not null,
                priority integer,
                place text not null,
                comment text not null,
		finished integer);"""

    cur.execute(table_create_sql)
    conn.close()
