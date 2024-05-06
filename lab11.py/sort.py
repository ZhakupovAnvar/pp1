import psycopg2 as pgsql

def sortingQuery(table_name, limit, offset):
    try:
        connection = pgsql.connect(
            database="phonebook",
            user='postgres',
            password='2305',
            host='localhost',
        )
        con = connection.cursor()
        query = f"SELECT * FROM {table_name} LIMIT %s OFFSET %s;"
        con.execute(query, (limit, offset))
        rows = con.fetchall()
        for row in rows:
            print(row)

    except pgsql.Error as e:
        print("Error", e)
    finally:
        if connection:
            con.close()
            connection.close()

sortingQuery('phones', limit=10, offset=0)