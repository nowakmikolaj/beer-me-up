import os
import json
from io import StringIO


def format(text):
    return f'\'{text}\''


def format_list(list):
    return map(lambda x: format(x), list)


class Beer:
    def __init__(self, style, name, alcohol, color, flavor, fermentation, carbonation, link):
        self.style = format(style)
        self.name = format(name)
        self.alcohol = format_list(alcohol)
        self.color = format_list(color)
        self.flavor = format_list(flavor)
        self.fermentation = format_list(fermentation)
        self.carbonation = format_list(carbonation)
        self.link = link

    def __repr__(self):
        return f"\n{self.style} - {self.name}"


with open('beers-data-split.json') as f:
    data = f.read()

beers_json = json.loads(data)

beers = []
for beer_dict in beers_json:
    beer = Beer(
        beer_dict['style'],
        beer_dict['name'],
        beer_dict['alcohol'],
        beer_dict['color'],
        beer_dict['flavor'],
        beer_dict['fermentation'],
        beer_dict['carbonation'],
        beer_dict['link']
    )
    beers.append(beer)

facts = StringIO()
for index, beer in enumerate(beers):
    with StringIO() as beer_facts:
        beer_facts.write(f'# Beer {index + 1}:\n')
        beer_facts.write(f'has_style({beer.name}, {beer.style})\n')
        for item in beer.alcohol:
            beer_facts.write(f'has_alcohol({beer.name}, {item})\n')
        for item in beer.color:
            beer_facts.write(f'has_color({beer.name}, {item})\n')
        for item in beer.flavor:
            beer_facts.write(f'has_flavor({beer.name}, {item})\n')
        for item in beer.fermentation:
            beer_facts.write(f'has_fermentation({beer.name}, {item})\n')
        for item in beer.carbonation:
            beer_facts.write(f'has_carbonation({beer.name}, {item})\n')

        beer_facts.write('\n')
        facts.write(beer_facts.getvalue())

filename = '../bases/facts.kfb'
os.makedirs(os.path.dirname(filename), exist_ok=True)
with open(filename, 'w') as f:
    f.write(facts.getvalue())

f.close()
