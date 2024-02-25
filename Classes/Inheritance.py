# Inheritance in class :-

    # class Car():
    #     def __init__(self, year, model, name) -> None:
    #         self.odometer = 0
    #         self.year = year
    #         self.model = model
    #         self.name = name
    #     def describe_car(self):
    #         long_name = str(self.year) + " " + self.name.upper() + " " + str(self.model.title())
    #         return long_name.title()
    #     def read_odometer(self):
    #         print("The odometer reading is " + str(self.odometer))
    #     def update_odometer(self, milage):
    #         self.odometer = milage
    # class ElectricCar(Car):
    #     def __init__(self, year, model, name) -> None:
    #         super().__init__(year, model, name)
    # my_tesla = ElectricCar(2022, "model 's'", 'tesla')
    # print(my_tesla.describe_car())




# Adding Attributes & Methods to Child Class :-

    # class Car():
        # def __init__(self, name) -> None:
            # self.name = name
        # def describe_car(self):
            # car_name = self.name
            # return car_name.title()
    # class Electric_car(Car):
        # def __init__(self, name) -> None:
            # super().__init__(name)
            # self.battery = 72
        # def battery_info(self):
            # info = 'The battery is marked with ' + str(self.battery) + " KWH"
            # return info
    # my_car = Electric_car('tesla')
    # print(my_car.battery_info())




# OverRiding a Method from the parent class :

    # class Car():
        # def __init__(self, name) -> None:
            # self.name = name
        # def describe_fuel_car(self):
            # fuel_car_name = "It's my " + str(self.name)
            # return fuel_car_name
        # def fuel_status(self, fuel):
            # self.fuel = fuel
            # fuel_stat = "Your tank is " + str(self.fuel) + "%" + " filled"
            # return fuel_stat
    # my_car = Car('Tesla')
    # print(my_car.fuel_status(73))
    # print() 
    # class Electric_car(Car):
        # def __init__(self, name) -> None:
            # super().__init__(name)
        # def fuel_status(self, fuel):
            # print("Common, it's a battery powered car!")
    # Electric_car('Tesla').fuel_status('')