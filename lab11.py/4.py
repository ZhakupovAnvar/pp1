import psycopg2 as pgsql

def insert_many_users():
    try:
        connection = pgsql.connect(
            database="phonebook",
            user='postgres',
            password='2305',
            host='localhost',
        )
        con = connection.cursor()

        con.execute(r"""
            CREATE OR REPLACE FUNCTION many_users(names TEXT[], surnames TEXT[], phones TEXT[]) RETURNS TEXT[] AS $$
            DECLARE
                incorrect_data TEXT[];
                i INT := 1;
            BEGIN
                WHILE i <= array_length(names, 1) LOOP
                    IF length(phones[i]) <> 10 OR NOT phones[i] ~ '^\d+$' THEN
                        incorrect_data := array_append(incorrect_data, names[i] || ' - ' || phones[i]);
                    ELSE
                        INSERT INTO phones (name, surname, number) VALUES (names[i], surnames[i], phones[i]);
                    END IF;
                    i := i + 1;
                END LOOP;
                RETURN incorrect_data;
            END;
            $$ LANGUAGE plpgsql;
        """)

        connection.commit()
        print("Stored procedure created successfully!")

    except pgsql.Error as e:
        print("Error while connecting to PostgreSQL", e)
    finally:
        if connection:
            con.close()
            connection.close()

def many_users(names, surnames, phones):
    try:
        connection = pgsql.connect(
            database="phonebook",
            user='postgres',
            password='2305',
            host='localhost',
        )
        con = connection.cursor()

        con.callproc('many_users', (names, surnames, phones))
        incorrect_data = con.fetchone()

        if incorrect_data:
            print("Incorrect Data:")
            for data in incorrect_data:
                print(data)
        else:
            print("All users inserted successfully!")

        connection.commit()

    except pgsql.Error as e:
        print("Error while connecting to PostgreSQL", e)
    finally:
        if connection:
            con.close()
            connection.close()

insert_many_users()
names = ['Nuriman', 'Maksim']
surnames = ['Baltabayev', 'Agafonov']
phones = ['0010','89034']
many_users(names, surnames, phones)