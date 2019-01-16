import os
import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relation
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from datasource_settings import Base
from datasource_session import SessionContext


class Employee(Base):
    # テーブル名やカラム定義は必須
    __tablename__ = 'employee'
    id = Column(String(5), primary_key=True)
    name = Column(String(100))
    age = Column(Integer)

    def __str__(self):
        return '[id={}, name={}, age={}]'.format(self.id, self.name, self.age)

    @staticmethod
    def get_employee_all(limit=10):
        with SessionContext() as session:
            return session.query(Employee)\
                .limit(limit).all()

