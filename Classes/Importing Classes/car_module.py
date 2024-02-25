class Car():
    def __init__(self, name, model, year) -> None:
        self.name = name
        self.model = model
        self.year = year
        self.odometer = 34

    def describe_car(self):
        full_name = str(self.year) + " " + str(self.name) + " " + str(self.model)
        return full_name.title()
    
    def odometer_reading(self):
        print("The odometer has " + str(self.odometer) + " on its reading")
    
    def check_new_reading(self, milage):
        if milage >= self.odometer:
            self.odometer = milage
        
        else:
            print("You can't roll back on odometer!")
    
    def update_odometer(self, miles):
        self.odometer += miles
    
class Electric_Car():
    def __init__(self, name, model, year) -> None:
        self.name = name
        self.model = model
        self.year = year
    
    def describe_car(self):
        E_Car_Name = str(self.name) + ' ' + str(self.model) + ' ' + str(self.year)
        return E_Car_Name.title()
    
    def battery(self):
        B_Backup = "This car can run upto 150 KM on a single charge"
        return B_Backup