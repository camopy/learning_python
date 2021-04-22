class Date:
    def __init__(self, month, day, year):
        self.month = month
        self.day = day
        self.year = year

    def format(self):
        return f"{self.month}/{self.day}/{self.year}"


date = Date(4, 18, 2021)
print(date.format())