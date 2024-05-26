import psycopg2


# Функция, создающая структуру БД (таблицы).
def create_db(cur):
    cur.execute(
        """
    CREATE TABLE IF NOT EXISTS base_client(
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(20) NOT NULL,
        last_name VARCHAR(20) NOT NULL,
        email VARCHAR(30) NOT NULL UNIQUE
    );"""
    )

    cur.execute(
        """
    CREATE TABLE IF NOT EXISTS base_client_phone(
        client_id INTEGER REFERENCES base_client(id),
        phone VARCHAR(12) UNIQUE
    );"""
    )


# Функция, позволяющая добавить нового клиента.
def add_client(cur, id, first_name, last_name, email, phone=None):
    cur.execute(
        """
    INSERT INTO base_client(
        id,
        first_name,
        last_name,
        email)
        VALUES(%s, %s, %s, %s);""",
        (id, first_name, last_name, email),
    )

    cur.execute(
        """
    INSERT INTO base_client_phone(
        client_id,
        phone)
        VALUES(%s, %s);""",
        (id, phone),
    )


# Функция, позволяющая добавить телефон для существующего клиента.
def add_phone(cur, client_id, phone):
    cur.execute(
        """
    INSERT INTO base_client_phone(
        client_id,
        phone)
        VALUES(%s, %s);""",
        (client_id, phone),
    )


# Функция, позволяющая изменить данные о клиенте.
def change_client(cur, client_id, first_name, last_name, email, phone):
    cur.execute(
        """
    UPDATE base_client SET
        first_name=%s, last_name=%s, email=%s WHERE id=%s;""",
        (first_name, last_name, email, client_id),
    )

    cur.execute(
        """
    UPDATE base_client_phone SET phone=%s WHERE client_id=%s;""",
        (phone, client_id),
    )


# Функция, позволяющая удалить телефон для существующего клиента.
def delete_phone(cur, client_id, phone):
    cur.execute(
        """
    DELETE FROM base_client_phone WHERE client_id = %s AND phone = %s;""",
        (client_id, phone),
    )


# Функция, позволяющая удалить существующего клиента.
def delete_client(cur, client_id):
    cur.execute(
        """
    DELETE FROM base_client_phone WHERE client_id = %s;""",
        (client_id,),
    )

    cur.execute(
        """
    DELETE FROM base_client WHERE id = %s;""",
        (client_id,),
    )


# Функция, позволяющая найти клиента по его данным: имени, фамилии, email или телефону.
def find_client(cur, first_name=None, last_name=None, email=None, phone=None):
    cur.execute(
        """
    SELECT * FROM base_client
    JOIN base_client_phone ON base_client.id = base_client_phone.client_id
    WHERE (first_name = %(first_name)s or %(first_name)s IS NULL)
    AND (last_name = %(last_name)s or %(last_name)s IS NULL)
    AND (email = %(email)s or %(email)s IS NULL)
    AND (phone = %(phone)s or %(phone)s IS NULL);""",
        {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "phone": phone,
        },
    )

    print(cur.fetchall())


if __name__ == "__main__":
    with psycopg2.connect(
        database="netology_db", user="postgres", password="ugohos12"
    ) as conn:
        with conn.cursor() as cur:

            # create_db(cur)

            # add_client(cur, 1, "Иван", "Иванов", "ivan@ya.ru", "123456789")
            # add_client(cur, 2, "Петр", "Петров", "petr@ya.ru", "987654321")
            # add_client(cur, 3, "Сидор", "Сидоров", "sidor@ya.ru")
            # add_client(cur, 4, "Вася", "Васильев", "vasya@ya.ru")

            # add_phone(cur, 3, "684798516")
            # add_phone(cur, 4, "684168668")

            # change_client(cur, 1, "Олег", "Иванов", "ivan@ya.ru", "123456789")

            # delete_phone(cur, 3, "684798516")

            # delete_client(cur, 2)

            find_client(cur, "Вася")

    conn.close()
