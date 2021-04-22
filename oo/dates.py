from datetime import datetime, timedelta


class Date:
    def __init__(self):
        self.date = datetime.today()

    def format(self):
        return self.date.strftime("%d/%m/%Y %H:%M")


date = Date()
print(date.format())