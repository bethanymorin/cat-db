from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from __init__ import Base


class CatToyAssociation(Base):
    """ Table that associates Cats to their favorite CatToys
        and assigned a preference level
    """
    __tablename__ = 'cat_toy_association'

    cat_id = Column(Integer, ForeignKey('cat.id'), primary_key=True)  # foreign key to cat table
    cat_toy_id = Column(Integer, ForeignKey('cat_toy.id'), primary_key=True)  # foreign key to cat_toy table
    preference_level = Column(Integer)  # integer value representing cat's preference for the toy

    # relationship manager linking cat toys to their cat associations
    cat_toy = relationship("CatToy", back_populates="cat_toy_associations")

    # relationship manager linking cats to their cat toy associations
    cat = relationship("Cat", back_populates="cat_toy_associations")

    def __repr__(self):
        return "<CatToyAssociation(cat: %s, toy: %s, preference: %s)>" % (
            self.cat.name, self.cat_toy.name, self.preference_level
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
        "CatToyAssociation",
        back_populates='cat'
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
        "CatToyAssociation",
        back_populates='cat_toy'
    )

    def __repr__(self):
        return "<CatToy('%s')>" % self.name
