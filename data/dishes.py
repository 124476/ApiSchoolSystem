import sqlalchemy

from .db_session import SqlAlchemyBase


class Dish(SqlAlchemyBase):
    __tablename__ = 'dishes'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    count = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    isHere = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True)
    schoolId = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
