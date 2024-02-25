class Phone():
    def __init__(self, name, model, memory, ram) -> None:
        self.name = name
        self.model = model
        self.memory = memory
        self.ram = ram
    
    def phone_specs(self):
        specs = str(self.name) + " " + str(self.model) + " " + str(self.memory) + " " + str(self.ram)
        return specs.title()
    
class Battery():
    def __init__(self) -> None:
        self.battery_health = "100%"
        self.battery_capacity = '5000 mah'
    
    def battery_health_stat(self):
        status = str(self.battery_health)
        return status
    
    def battery_capacity_stat(self):
        status = str(self.battery_capacity)
        return status
    
class Charger():
    def __init__(self) -> None:
        self.charger = 25

    def charger_stat(self):
        status = str(self.charger) + " " + "watt"
        return status
    
class Merge(Phone):
    def __init__(self, name, model, memory, ram) -> None:
        super().__init__(name, model, memory, ram)
        self.battery = Battery()
        self.charger = Charger()

my_phone = Merge("Samsung", 'Galaxy S23 Ultra', '512 GB', "8 GB")
print()
print(my_phone.phone_specs())
print()
print("It's Battery Health is " + my_phone.battery.battery_health_stat())
print("It's Battery Capacity is " + my_phone.battery.battery_capacity_stat())
print()
print("It comes with a charger of " + my_phone.charger.charger_stat())
print()