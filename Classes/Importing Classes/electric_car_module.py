# Importing a module into a module

from car_module import Car

class Battery():
    def __init__(self, battery_stat = 84) -> None:
        self.battery = battery_stat
    def describe_battery(self):
        print("The battery status is " + str(self.battery))
class Electric_car(Car):
    def __init__(self, name, model, year) -> None:
        super().__init__(name, model, year)
        self.bat = Battery()
# my_tesla = Electric_car('Tesla', 'model 3', '2023')
# print(my_tesla.describe_car())
# my_tesla.bat.describe_battery()