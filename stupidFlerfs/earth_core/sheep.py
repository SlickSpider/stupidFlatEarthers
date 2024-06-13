"""
Main class for sheeps(flerfs)
"""
# globals
SHEEP_SLANG = 'flerf'


class Sheep(object):
    def __init__(self, name: str) -> None:
        self.name = name
        self.papa = None
        self.email = None
        self.discord = None
        self.http = None

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

    @property
    def email(self) -> str:
        return self.email

    @email.setter
    def email(self, email: str) -> None:
        self.email = email

    @property
    def discord(self) -> str:
        return self.discord

    @discord.setter
    def discord(self, discord: str) -> None:
        self.discord = discord

    @property
    def http(self) -> str:
        return self.http

    @http.setter
    def http(self, http: str) -> None:
        self.http = http
