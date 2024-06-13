"""
Main class for sheeps(flerfs)
"""
SHEEP_SLANG = 'flerf'


class Sheep(object):
    def __init__(self, name: str) -> None:
        self.name = name
        self.papa = None

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        return f'{class_name}({self.name})'

    @property
    def name(self) -> str:
        return self.name

    @name.setter
    def name(self, name: str) -> None:
        self.name = name

    @property
    def papa(self) -> str:
        return self.papa

    @papa.setter
    def papa(self, papa: str) -> None:
        self.papa = papa

