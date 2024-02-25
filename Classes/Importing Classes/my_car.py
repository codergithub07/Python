# Importing a Class from a module

    # from car_module import Car

        # new_car = Car('audi', 'a8', '2019')
        # print(new_car.describe_car())
        # print()
        # new_car.check_new_reading(43)
        # new_car.odometer_reading()
        # print()
        # new_car.update_odometer(7)
        # new_car.odometer_reading()
        # print()




# Importing multiple Classes from a module

    # from car_module import Car, Electric_Car

        # new_car = Car('audi', 'a8', '2019')
        # print(new_car.describe_car())
        # print()
        # new_car.check_new_reading(43)
        # new_car.odometer_reading()
        # print()
        # new_car.update_odometer(7)
        # new_car.odometer_reading()
        # print()
        # my_tesla = Electric_Car('Tesla', 'Model 3', '2022')
        # print(my_tesla.describe_car())
        # print()
        # print(my_tesla.battery())




# Importing entire module

    # import car_module

        # my_car = car.Car('Accent', 'V2', '2024')
        # print(my_car.describe_car())
        # print()
        # my_tesla = car.Electric_Car('Tesla', 'model 3', '2023')
        # print(my_tesla.describe_car())




# Importing all Classes from a module

    # from car_module import *

        # my_car = Car('Hyundai', 'Accent', '2013')
        # print(my_car.describe_car())

    # NOTE :- This method is not recommended because it creats confusion about which classes are being used
    #         & also it might creat conflict when same name is used in our program as in the module class




# import car_module
# import electric_car_module

# my_car = car_module.Car('Hyundai', 'Accent', '2023')
# print(my_car.describe_car())
# my_tesla = electric_car_module.Electric_car('Tesla', 'X3', '2023')
# print(my_tesla.describe_car())