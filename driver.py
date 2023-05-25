import sys

from pyke import knowledge_engine
from pyke import krb_traceback
from models.beer import Beer
from models.beer_info import BeerInfo
import os

display_count = 5


def run_driver():
    engine = knowledge_engine.engine(__file__)
    engine.reset()

    engine.activate('rules')

    os.system('clear')

    print('----------------------')
    print("Welcome to Beer-Me-Up!")
    print('----------------------')

    try:
        beers = []
        with engine.prove_goal(
                'rules.beer($beer, $link, $explanation)') as gen:

            # Get beers
            i = 0
            for vars, plan in gen:
                i = i + 1
                beer = Beer(vars['beer'], vars['link'], vars['explanation'])
                beers.append(beer)

        # Get unique beers
        keys = list(set(beers))
        print('\nGenerating result...\n')
        print(f'{len(keys)} beers found.\n')

        # Create dictionary
        dictionary = {}
        for beer in beers:
            if dictionary.get(beer.name) is not None:
                dictionary[beer.name].add(beer.explanation)
            else:
                dictionary[beer.name] = BeerInfo(beer)

        # Sort dictionary - descending by count
        dictionary = dict(
            sorted(dictionary.items(), key=lambda item: -item[1].count))

        # Display top X results
        print(f'Prepared {display_count} beers for you:')
        result = list(dictionary.values())
        for index, beer in enumerate(result[0:display_count]):
            print(f'#{index+1} {beer}\n')

    except Exception:
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    run_driver()
