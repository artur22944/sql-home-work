CREATE TABLE IF NOT EXISTS Жанр (
	id SERIAL PRIMARY key,
	Название_жанра VARCHAR(40) NOT null
);

CREATE TABLE IF NOT EXISTS Исполнитель (
	id SERIAL PRIMARY key,
	Имя_Псевдоним VARCHAR(40) NOT NULL
);

CREATE TABLE IF NOT EXISTS Альбом (
	id SERIAL PRIMARY key,
	Название_альбома VARCHAR(40) NOT null,
	Год_выпуска_альбома integer not NULL
);

CREATE TABLE IF NOT exists Трэк (
	ID SERIAL PRIMARY key,
	Название_трэка VARCHAR(40) NOT null,
	Длительность_трэка integer,
	Альбом_ID INTEGER references Альбом(id)
);

CREATE TABLE IF NOT exists Сборник (
	id SERIAL PRIMARY key,
	Название_сборника VARCHAR(40) NOT null,
	Год_выпуска_сборника integer
);

CREATE TABLE IF NOT EXISTS Жанр_Исполнитель (
	Жанр_ID INTEGER NOT NULL references Жанр(id),
	Исполнитель_ID INTEGER NOT NULL references Исполнитель(id),
    primary key (Жанр_ID, Исполнитель_ID)
);

CREATE TABLE IF NOT EXISTS Исполнитель_Альбом (
	Исполнитель_ID INTEGER NOT NULL references Исполнитель(id),
	Альбом_ID INTEGER NOT NULL references Альбом(id),
    primary key (Исполнитель_ID, Альбом_ID)
);

CREATE TABLE IF NOT EXISTS Трэк_Сборник (
	Трэк_ID INTEGER NOT NULL references Трэк(id),
	Сборник_ID INTEGER NOT NULL references Сборник(id),
    primary key (Трэк_ID, Сборник_ID)
);
