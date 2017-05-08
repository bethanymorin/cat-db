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
        ]

        gwens_favorite_toys = ['owl', 'rainbow', 'parrot', 'carrot']
        deweys_favorite_toys = ['tunnel', 'shaky mouse', 'parrot', 'hair tie']

        for toy in cat_toys:
            new_toy = CatToy(name=toy)
            self.session.add(new_toy)
            if toy in deweys_favorite_toys:
                dewey.toys.append(new_toy)
            if toy in gwens_favorite_toys:
                gwen.toys.append(new_toy)
        self.session.commit()
        gwens_toys = self.session.query(CatToy).filter(CatToy.cats.contains(gwen)).all()

        gwens_toys_list = [toy.name for toy in gwens_toys]

        self.assertEqual(set(gwens_toys_list), set(gwens_favorite_toys))
