from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from __init__ import Base
from unittest import TestCase
from models import Cat, CatToy, CatToyAssociation


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
        self.session.commit()
        cat_toys = [
            'tunnel',
            'owl',
            'shaky mouse',
            'parrot',
            'rainbow',
            'carrot',
            'hair tie',
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
            self.session.commit()
            if toy in deweys_favorite_toys:
                ct_assoc = CatToyAssociation(
                    cat_id=dewey.id,
                    cat_toy_id=new_toy.id,
                    preference_level=deweys_favorite_toys[toy],
                )
                self.session.add(ct_assoc)
            if toy in gwens_favorite_toys:
                ct_assoc = CatToyAssociation(
                    cat_id=gwen.id,
                    cat_toy_id=new_toy.id,
                    preference_level=gwens_favorite_toys[toy],
                )
                self.session.add(ct_assoc)

        self.session.commit()
        gwens_toys_query = self.session.query(CatToyAssociation)
        gwens_toys_query = gwens_toys_query.filter(CatToyAssociation.cat == gwen)
        gwens_toys_query = gwens_toys_query.filter(CatToyAssociation.preference_level == 1)
        gwens_toys_query = gwens_toys_query.all()

        for toy_obj in gwens_toys_query:
            self.assertTrue(toy_obj.cat_toy.name in gwens_favorite_toys)
            self.assertEqual(toy_obj.preference_level, gwens_favorite_toys[toy_obj.cat_toy.name])
