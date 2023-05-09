from .beer import Beer


class BeerInfo(Beer):
    def __init__(self, beer):
        self.name = beer.name
        self.link = beer.link
        self.explanation = beer.explanation
        self.count = 0

    def add(self, explanation):
        self.count += 1
        if explanation not in self.explanation:
            self.explanation += explanation
