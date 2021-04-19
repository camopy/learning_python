from tvshow import Tvshow


class Movie(Tvshow):
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self._duration = duration

    @property
    def duration(self):
        return self._duration

    def __str__(self):
        return f"{self._name.title()} - {self._year} - {self._duration} min - {self._likes} Likes"