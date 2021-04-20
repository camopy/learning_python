class Employee:
    def __init__(self, name):
        self.name = name

    def log_hours(self, horas):
        print("Logged hours.")

    def show_tasks(self):
        print("Did many things...")


class Caelum(Employee):
    def show_tasks(self):
        print("Did many things, Caelumer")

    def search_month_courses(self, month=None):
        print(f"Showing courses - {month}" if month else "Showing this month courses")


class Alura(Employee):
    def show_tasks(self):
        print("Did many things, Alurete!")

    def search_unanswered_questions(self):
        print("Showing forums's unanswered questions")


class Hipster:
    def __str__(self):
        return f"Hipster,  {self.name}"


class Junior(Alura):
    pass


class Middle(Alura, Caelum, Hipster):
    pass


amanda = Junior("Amanda")
amanda.search_unanswered_questions()
amanda.show_tasks()

paulo = Middle("Paulo")
paulo.search_month_courses()
paulo.search_unanswered_questions()
paulo.show_tasks()

print(amanda)
print(paulo)