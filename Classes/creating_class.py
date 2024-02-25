# Example 1 : Dog Class

    # class Dog():
        # def __init__(self, n, a):
            # self.name = n
            # self.age = a
        # def sit(self):
            # print(self.name.title() + " is now sitting")
        # def dog_age(self):
            # print(self.name.title() + "'s age is " + self.age)
    # my_dog = Dog('rob', '8')
    # print(my_dog.name.title() + "'s age is " + my_dog.age)
    # my_dog.sit()




# Example 2 : Restaurant Class

    # class Restaurant():
        # def __init__(self, restaurant_name, causine_type):
            # self.name = restaurant_name
            # self.type = causine_type
        # def restaurant_open(self):
            # print("We are now open to serve our Guests")
        # def describe_restaurant(self):
            # print("Our Restaurant's name is : " + self.name.title())
            # print("we are a " + self.type + " restaurant")
    # restaurant = Restaurant('rumine', 'fast food')
    # restaurant.restaurant_open()
    # restaurant.describe_restaurant()




# Example 3 :

    # class Car():
        # def __init__(self, name, model, year):
            # self.name = name
            # self.model = model
            # self.year = year
            # self.odometer = 0
        # def describe_car(self):
            # long_name = str(self.year) + ' ' + str(self.name) + ' ' + str(self.model)
            # return long_name.title()
        # def car_odometer(self):
            # print("This car has " + str(self.odometer) + " reading on it's odometer")
    # car_detail = Car('Audi', 'a8', '2016')
    # print(car_detail.describe_car())
    # car_detail.car_odometer()




# Changing an attribute value :-

    # Method 1 : Changing by directly accessing through an instance

        # class Car():
            # def __init__(self, name, model, year):
                # self.name = name
                # self.model = model
                # self.year = year
                # self.odometer = 0
            # def describe_car(self):
                # long_name = str(self.year) + ' ' + str(self.name) + ' ' + str(self.model)
                # return long_name.title()
            # def car_odometer(self):
                # print("This car has " + str(self.odometer) + " shown on it's odometer")
        # car_detail = Car('Audi', 'a8', '2016')
        # print(car_detail.describe_car())
        # car_detail.odometer = 20 # The odometer attribute is accessed at this instance
        # car_detail.car_odometer()

    # Method 2 : Modifying attribute value through a method

        # class Car():
            # def __init__(self, year, model, name) -> None:
                # self.odometer = 0
                # self.year = year
                # self.model = model
                # self.name = name
            # def describe_car(self):
                # long_name = str(self.year) + " " + self.name.upper() + " " + str(self.model.title())
                # print(long_name)
            # def read_odometer(self):
                # print("The odometer reading is " + str(self.odometer))
            # def update_odometer(self, milage):
                # self.odometer = milage
        # my_car = Car('2019', 'a7', 'bmw')
        # my_car.describe_car()
        # my_car.read_odometer()
        # my_car.update_odometer(56)
        # my_car.read_odometer()