import sqlite3
import sys
import os

def execute_query(sql: str) -> list:
    with sqlite3.connect('university.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

def main() -> None:
    if len(sys.argv) < 2 or len(sys.argv) > 2:
        print("Usage: python runSQL.py query_X.sql")
        sys.exit(1)

    source_file = sys.argv[1]

    if not os.path.exists(source_file):
        print("I didn't find this catalog.")
        sys.exit(1)
    with open(source_file, encoding = 'utf-8') as f:
        sql_query = f.read()

    print(execute_query(sql_query))


if __name__ == '__main__':
    main()