import sqlite3

def main():
    print('Create DB connection')
    db = sqlite3.connect('My_DB-API.db')
    cur = db.cursor()
    cur.execute('DROP TABLE IF EXISTS my_table')
    cur.execute("""
        CREATE TABLE my_table (
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT
        )
        """)
    cur.execute("""
        INSERT INTO my_table (first_name, last_name)
        VALUES ('Ivan', 'Petrov'),
               ('Petr', 'Ivanov')
        """)
    db.commit()
    cur.execute("""
        SELECT COUNT(*)
        FROM my_table
    """)
    res = cur.fetchone()[0]
    print(f'number of rows in my_table: {res}')
    print('\nContent of my_table:')
    for row in cur.execute('SELECT * FROM my_table'):
        print(row)
    db.close()





if __name__ == '__main__': main()