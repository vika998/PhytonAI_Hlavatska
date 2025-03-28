class person:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print(f"Привіт мене звати {self.name} ")


class student:
    def __init__(self, class_year):
        self.class_year = class_year

    def study(self):
        print(f"Я навчаюся в {self.class_year} класі.")


class worker:
    def __init__(self, job_name):
        self.job_name = job_name

    def work(self):
        print(f"Я працюю  як {self.job_name}")


class student_worker(person, student, worker):
    def __init__(self, name, class_year, job_name):
        person.__init__(self, name)
        student.__init__(self, class_year)
        worker.__init__(self, job_name)

person = student_worker("Віка", 7,"ахітектор" )

person.hello()
person.study()
person.work()