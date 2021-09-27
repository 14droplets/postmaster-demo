from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import String, Integer, DateTime


Base = declarative_base()


# Про базы данных много документации тут https://flask-sqlalchemy.palletsprojects.com/en/2.x/
# А чтобы СОВСЕМ МНОГО - вот тут https://www.sqlalchemy.org/


class Post(Base):
    """ ORM  Модель постов, которые нужно сделать """

    id = Column(Integer, primary_key=True, nullable=False)
    """ Первичное поле таблицы - уникальный номер записи """

    description = Column(String, nullable=False)
    """ Описание поста. Собственно текст как он есть """

    tags = Column(String, nullable=True)
    """ Тэги поста, сделаем их в виде строки через запятую. 
        Вообще-то это нарушение первой нормальной формы БД и это плохо, 
        но для простого примера, сделаем так """

    publication_date = Column(DateTime, nullable=False)
    """ Дата публикации """

    # Дальше идут поля, необходимые для алхимии
    __tablename__ = "posts"
    """ имя таблицы """
