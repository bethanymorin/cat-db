from models import Cat, CatToy
from __init__ import Base, engine, session

Base.metadata.create_all(bind=engine)

gwen = Cat(
    name='Gwen',
    age=19,
    gender='f',
    coloring='tuxedo'
)

session.add(gwen)

dewey = Cat(
    name='Dewey',
    age=5,
    gender='m',
    coloring='buff tabby'
)

session.add(dewey)

cats = session.query(Cat).all()
print "You have %d cats" % len(cats)

for cat in cats:
    print cat

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
    session.add(new_toy)
    if toy in deweys_favorite_toys:
        dewey.toys.append(new_toy)
    if toy in gwens_favorite_toys:
        gwen.toys.append(new_toy)

print "\n"
print "Dewey's favorite toys are: "
for toy in dewey.toys:
    print toy
print "\n"
print "Gwen's favorite toys are: "
for toy in gwen.toys:
    print toy
print "\n"
