from datetime import datetime, timedelta


class Date:
    def __init__(self, date):
        self.date = date

    def format(self):
        return self.date.strftime("%d/%m/%Y %H:%M")

    def time_from_date(self, date):
        return date - self.date

    def __str__(self):
        return self.format()


today = Date(datetime.today())
one_week_later = datetime.today() + timedelta(days=7)

print("Now:", today)
print("1 week later:", Date(one_week_later))

print("Time between:", today.time_from_date(one_week_later))