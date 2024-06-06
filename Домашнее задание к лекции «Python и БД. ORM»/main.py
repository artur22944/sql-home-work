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
create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()


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


def get_shops(name):
    query = (
        session.query(Book.title, Shop.name, Sale.price, Sale.date_sale)
        .select_from(Shop)
        .join(Stock)
        .join(Book)
        .join(Publisher)
        .join(Sale)
    )
    if name.isdigit():
        name = int(name)
        result = query.filter(Publisher.id == name).all()
    else:
        result = query.filter(Publisher.name == name).all()
    for title, name, price, date_sale in result:
        print(
            f"{title: <40} | {name: <10} | {price: <8} | {date_sale.strftime('%d.%m.%Y')}"
        )


if __name__ == "__main__":
    name = input("Введите имя издателя: ")
    get_shops(name)


drop_tables(engine)

session.close()
