from tvshow import Tvshow


class Movie(Tvshow):
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self._duration = duration

    @property
    def duration(self):
        return self._duration