from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from __init__ import Base


cat_toy_association_table = Table(
    'cat_toy_association',
    Base.metadata,
    Column('cat_id_id', Integer, ForeignKey('cat.id')),
    Column('cat_toy_id', Integer, ForeignKey('cat_toy.id'))
)


class Cat(Base):
    __tablename__ = 'cat'

    id = Column(Integer, primary_key=True, autoincrement=True)

    # properties of a cat
    name = Column(String)
    age = Column(Integer)
    coloring = Column(String)
    gender = Column(String)

    # relationship manager linking Cat to CatToyAssociation
    # allows you to call Cat().toy_associations and get back all CatToyAssociation
    # objects linked to that Cat
    cat_toy_associations = relationship(
        "CatToy",
        secondary=cat_toy_association_table
    )

    def __repr__(self):
        return "<Cat(%s, %s, %s)>" % (self.name, self.age, self.coloring)


class CatToy(Base):
    __tablename__ = 'cat_toy'

    id = Column(Integer, primary_key=True, autoincrement=True)

    # properties of a cat toy
    name = Column(String)

    # relationship manager between CatToys and CatToyAssociation
    # allows you to call CatToy().cat_associations and get back all CatToyAssociation
    # objects linked to that toy
    cat_toy_associations = relationship(
        "Cat",
        secondary=cat_toy_association_table
    )

    def __repr__(self):
        return "<CatToy('%s')>" % self.name
