class Human:
    def __init__(self, name = "Human"):
        self.name = name

class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passenger(self, human):
        self.passengers.append(human)

    def print_passangers_names(self):
        if self.passengers !=[]:
            print(f"Names of {self.brand} passengers:")
            for passenger in self.passengers:
                print(passenger.name)
        else:
            print(f"There are no passengers is {self.brand}")

nick = Human("Nick")
kate = Human("Kate")
car = Auto("Mercedes")
car.add_passenger(nick)
car.add_passenger(kate)
car.print_passangers_names()

print("-"*30)

tom = Human("Tom")
alex = Human("Alex")
bill = Human("Bill")
lisa = Human("Lisa")
luka = Human("Luka")
car = Auto("BWM")
car.add_passenger(tom)
car.add_passenger(alex)
car.add_passenger(bill)
car.add_passenger(lisa)
car.add_passenger(luka)
car.print_passangers_names()
