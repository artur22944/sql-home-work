import psycopg2


# Функция, создающая структуру БД (таблицы).
def create_db(cur):
    cur.execute("""
    CREATE TABLE if not exists BASE_CLIENTS(
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(20) NOT NULL,
        last_name VARCHAR(20) NOT NULL,
        email VARCHAR(30) NOT NULL UNIQUE,
        phone VARCHAR(20)
    );
    """)
    print(cur.fetchall)


# Функция, позволяющая добавить нового клиента.
def add_client(cur, first_name, last_name, email, phones=None):
    cur.execute("""
    INSERT INTO BASE_CLIENTS(
        first_name,
        last_name,
        email,
        phone)
        VALUES(%s, %s, %s, %s);""", (first_name, last_name, email, phones))
    print(cur.fetchall)


# Функция, позволяющая добавить телефон для существующего клиента.
def add_phone(cur, client_id, phone):
    cur.execute("""
    UPDATE BASE_CLIENTS SET phone = %s WHERE id = %s;""", (phone, client_id))
    print(cur.fetchall)


# Функция, позволяющая изменить данные о клиенте.
def change_client(cur, client_id, first_name=None, last_name=None, email=None, phones=None):
    cur.execute("""
    UPDATE BASE_CLIENTS SET first_name = %s, last_name = %s, email = %s, phone = %s WHERE id = %s;""", (first_name, last_name, email, phones, client_id))
    cur.execute("""SELECT * FROM BASE_CLIENTS;""")
    print(cur.fetchall())


# Функция, позволяющая удалить телефон для существующего клиента.
def delete_phone(cur, phone):
    conn.execute("""DELETE FROM BASE_CLIENTS WHERE phone=%s;""", (phone,))
    print(cur.fetchall())


# Функция, позволяющая удалить существующего клиента.
def delete_client(cur, client_id):
    cur.execute("""
    DELETE FROM BASE_CLIENTS WHERE id = %s;""", (client_id, ))
    cur.execute("""SELECT * FROM BASE_CLIENTS;""")
    print(cur.fetchall())


# Функция, позволяющая найти клиента по его данным: имени, фамилии, email или телефону.
def find_client(cur, first_name=None, last_name=None, email=None, phone=None):
    cur.execute("""
    SELECT * FROM BASE_CLIENTS WHERE first_name = %s OR last_name = %s OR email = %s OR phone = %s;""", (first_name, last_name, email, phone))
    print(cur.fetchall())


if __name__ == "__main__":
    with psycopg2.connect(database="netology_db",
                          user="postgres",
                          password="ugohos12") as conn:
        with conn.cursor() as cur:

            # create_db(cur)

            # add_client(cur, "Иван", "Иванов", "ivan@ya.ru", "123456789")
            # add_client(cur, "Петр", "Петров", "petr@ya.ru", "987654321")
            # add_client(cur, "Сидор", "Сидоров", "sidor@ya.ru")
            # add_client(cur, "Вася", "Васильев", "vasya@ya.ru")

            # add_phone(cur, 1, "684798516")
            # add_phone(cur, 3, "684168668")

            # change_client(cur, 1, first_name="Олег", last_name="Олегов", email="oleg@ya.ru", phones="165165165")

            # delete_phone(cur, "165165165")

            # delete_client(cur, 2)

            # find_client(cur, first_name="Вася")

    conn.close()
