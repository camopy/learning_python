class Playlist:
    def __init__(self, name, tvshows):
        self.name = name
        self._tvshows = tvshows

    def __getitem__(self, item):
        return self._tvshows[item]

    def __len__(self):
        return len(self._tvshows)