from .beer import Beer


class BeerInfo(Beer):
    def __init__(self, beer):
        super().__init__(beer.name, beer.link, beer.explanation)
        self.count = 1

    def add(self, explanation):
        self.count += 1
        if explanation not in self.explanation:
            self.explanation += explanation
