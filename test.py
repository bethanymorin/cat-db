from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from __init__ import Base
from unittest import TestCase
from models import Cat, CatToy


class BaseTest(TestCase):
    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(bind=self.engine)

        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def tearDown(self):
        Base.metadata.drop_all(bind=self.engine)


class TestModels(BaseTest):
    def test_cat_toy_relationships(self):
        gwen = Cat(
            name='Gwen',
            age=19,
            gender='f',
            coloring='tuxedo'
        )

        self.session.add(gwen)

        dewey = Cat(
            name='Dewey',
            age=5,
            gender='m',
            coloring='buff tabby'
        )

        self.session.add(dewey)
        cat_toys = [
            'tunnel',
            'owl',
            'shaky mouse',
            'parrot',
            'rainbow',
            'carrot',
            'hair tie',
            'wicker ball',
        ]

        gwens_favorite_toys = {
            'owl': 1,
            'rainbow': 1,
            'parrot': 2,
            'carrot': 3,
        }
        deweys_favorite_toys = {
            'tunnel': 1,
            'shaky mouse': 2,
            'parrot': 3,
            'hair tie': 1
        }

        for toy in cat_toys:
            new_toy = CatToy(name=toy)
            self.session.add(new_toy)
            if toy in deweys_favorite_toys:
                dewey.cat_toy_associations.append(new_toy)
            if toy in gwens_favorite_toys:
                gwen.cat_toy_associations.append(new_toy)

        for toy_association in gwen.cat_toy_associations:
            # with this, you can use exactly 1 step tp get from the toy
            # association object to the toy
            self.assertTrue(toy_association.name in gwens_favorite_toys)
