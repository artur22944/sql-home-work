import psycopg2


def create_db(conn):
    with psycopg2.connect(database="netology_db", user="postgres", password="ugohos12") as conn:
        with conn.cursor() as cur:
            cur.execute("""
            CREATE TABLE if not exists BASE_CLIENTS(
                id SERIAL PRIMARY KEY,
                first_name VARCHAR(20) NOT NULL,
                last_name VARCHAR(20) NOT NULL,
                email VARCHAR(30) NOT NULL UNIQUE,
                phone VARCHAR(20)
            );
            """)


def add_client(conn, first_name, last_name, email, phones=None):
    


def add_phone(conn, client_id, phone):
    pass


def change_client(conn, client_id, first_name=None, last_name=None, email=None, phones=None):
    pass


def delete_phone(conn, client_id, phone):
    pass


def delete_client(conn, client_id):
    pass


def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
    pass


with psycopg2.connect(database="clients_db", user="postgres", password="postgres") as conn:
    pass  # вызывайте функции здесь

conn.close()