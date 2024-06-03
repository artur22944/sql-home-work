import json

import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker
from models import Publisher, Shop, Book, Stock, Sale
from models import create_tables, drop_tables


login = input("Введите логин: ")
password = input("Введите пароль: ")
database = input("Введите название базы данных: ")

DNS = f"postgresql://{login}:{password}@localhost:5432/{database}"
engine = sq.create_engine(DNS)

Session = sessionmaker(bind=engine)
session = Session()
create_tables(engine)

with open("fixtures/tests_data.json", "r") as fd:
    data = json.load(fd)

    for record in data:
        model = {
            "publisher": Publisher,
            "shop": Shop,
            "book": Book,
            "stock": Stock,
            "sale": Sale,
        }[record.get("model")]
        session.add(model(id=record.get("pk"), **record.get("fields")))
    session.commit()

input_publisher = input("Введите имя издателя: ")
if input_publisher.isdigit():
    input_publisher = int(input_publisher)
    publisher = (
        session.query(Shop)
        .join(Stock.shops)
        .join(Book)
        .join(Publisher)
        .filter(Publisher.id == input_publisher)
        .all()
    )
else:
    publisher = (
        session.query(Shop)
        .join(Stock.shops)
        .join(Book)
        .join(Publisher)
        .filter(Publisher.name == input_publisher)
        .all()
    )
print(publisher)

drop_tables(engine)

session.close()
