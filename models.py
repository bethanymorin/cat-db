from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from __init__ import Base


class CatToyAssociation(Base):
    __tablename__ = 'cat_toy_association'
    cat_id = Column(Integer, ForeignKey('cat.id'), primary_key=True)
    cat_toy_id = Column(Integer, ForeignKey('cat_toy.id'), primary_key=True)
    preference_level = Column(Integer)
    cat_toy = relationship("CatToy", back_populates="cats")
    cat = relationship("Cat", back_populates="toys")

    def __repr__(self):
        return "<CatToyAssociation(cat: %s, toy: %s, preference: %s)>" % (
            self.cat.name, self.cat_toy.name, self.preference_level
        )


class Cat(Base):
    __tablename__ = 'cat'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    age = Column(Integer)
    coloring = Column(String)
    gender = Column(String)
    toys = relationship(
        "CatToyAssociation",
        back_populates='cat'
    )

    def __repr__(self):
        return "<Cat(%s, %s, %s)>" % (self.name, self.age, self.coloring)


class CatToy(Base):
    __tablename__ = 'cat_toy'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    cats = relationship(
        "CatToyAssociation",
        back_populates='cat_toy'
    )

    def __repr__(self):
        return "<CatToy('%s')>" % self.name
