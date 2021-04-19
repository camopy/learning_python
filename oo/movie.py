from tvshow import Tvshow


class Movie(Tvshow):
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.__duration = duration

    @property
    def duration(self):
        return self.__duration