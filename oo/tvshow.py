class Tvshow:
    def __init__(self, name, year):
        self._name = name
        self._year = year
        self._likes = 0

    @property
    def name(self):
        return self._name.title()

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def year(self):
        return self._year

    @property
    def likes(self):
        return self._likes

    def addLike(self):
        self._likes += 1

    def __str__(self):
        return f"{self._name.title()} - {self._year} - {self._likes} Likes"