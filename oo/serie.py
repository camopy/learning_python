from tvshow import Tvshow


class Serie(Tvshow):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self._seasons = seasons

    @property
    def seasons(self):
        return self._seasons