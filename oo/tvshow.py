class Tvshow:
    def __init__(self, name, year):
        self.__name = name
        self.__year = year
        self.__likes = 0

    @property
    def name(self):
        return self.__name.title()

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def year(self):
        return self.__year

    @property
    def likes(self):
        return self.__likes

    def addLike(self):
        self.__likes += 1