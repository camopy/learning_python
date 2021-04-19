from tvshow import Tvshow


class Serie(Tvshow):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self._seasons = seasons

    @property
    def seasons(self):
        return self._seasons

    def __str__(self):
        duration_string = "season" if self._seasons == 1 else "seasons"
        return f"{self._name.title()} - {self._year} - {self._seasons} {duration_string} - {self._likes} Likes"