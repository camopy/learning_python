class Date:
    def __init__(self, month, day, year):
        self.month = month
        self.day = day
        self.year = year

    def formated(self):
        return "{}/{}/{}".format(self.month, self.day, self.year)