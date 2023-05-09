class Beer:
    def __init__(self, name, link, explanation):
        self.name = name
        self.link = link
        self.explanation = explanation

    def __repr__(self):
        return f"{self.name} - {self.link} - {self.explanation}"

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        if isinstance(other, Beer):
            return self.name == other.name
        return NotImplemented
