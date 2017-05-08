from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from __init__ import Base


cat_toy_association_table = Table(
    'cat_toy_association',
    Base.metadata,
    Column('cat_id', Integer, ForeignKey('cat.id')),
    Column('cat_toy_id', Integer, ForeignKey('cat_toy.id'))
)


class Cat(Base):
    __tablename__ = 'cat'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    age = Column(Integer)
    coloring = Column(String)
    gender = Column(String)
    toys = relationship(
        "CatToy",
        secondary=cat_toy_association_table,
        back_populates='cats'
    )

    def __repr__(self):
        return "<Cat(%s, %s, %s)>" % (self.name, self.age, self.coloring)


class CatToy(Base):
    __tablename__ = 'cat_toy'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    cats = relationship(
        "Cat",
        secondary=cat_toy_association_table,
        back_populates='toys'
    )

    def __repr__(self):
        return "<CatToy('%s')>" % self.name
