import sqlalchemy

from .meta import Base


class Person(Base):
    __tablename__ = 'persons'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.Text)
    email = sqlalchemy.Column(sqlalchemy.Text)
    phone_number = sqlalchemy.Column(sqlalchemy.Text)
    covid_status = sqlalchemy.Column(sqlalchemy.Text)




