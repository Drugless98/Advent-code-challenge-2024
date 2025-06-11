from dataclasses import dataclass, field

@dataclass
class Between():
    first_level : int
    next_level  : int

    def __post_init__(self): 
        self.Ascending = self.first_level < self.next_level if abs(self.first_level - self.next_level) < 4 else False
        self.Descending= self.first_level > self.next_level if abs(self.first_level - self.next_level) < 4 else False
        self.Equal     = self.first_level== self.next_level

@dataclass
class Report:
    levels: list[str]

    def __post_init__(self): #: make the "in between levels" object
        self.between_levels = [Between(int(l_from), int(l_too)) for l_from, l_too in zip(self.levels[:-1], self.levels[1:])]
        self.Ascending_count  = [i.Ascending  for i in self.between_levels].count(True)
        self.Descending_count = [i.Descending for i in self.between_levels].count(True)

        self.Safe       = self.Ascending_count == len(self.levels) - 1 or self.Descending_count == len(self.levels) - 1
        self.SafeDamper = self.Ascending_count == len(self.levels) - 2 or self.Descending_count == len(self.levels) - 2