import re


class Phone:
    pattern = "([0-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4})"

    def __init__(self, number):
        if self.is_valid(number):
            self.number = number
        else:
            raise ValueError("Invalid phone number")

    def is_valid(self, number):
        regex = re.compile(self.pattern)
        return regex.match(number)

    def __str__(self):
        return self.format()

    def format(self):
        search = re.search(self.pattern, self.number)
        return f"+{search.group(1)} ({search.group(2)}) {search.group(3)}-{search.group(4)}"
