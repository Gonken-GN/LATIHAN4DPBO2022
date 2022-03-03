from vehicle import Vehicle
class Ship(Vehicle):
    def __init__(self):
        self.age = 0
        self.type = ""
        self.country = ""
    def setShip(self, fueltype, maxpasengger, age, type, country):
        self.setVehicle(fueltype, maxpasengger)
        self.setBoolean(1)
        self.age = age
        self.type = type
        self.country = country
    def getAge(self):
        return self.age
    def getType(self):
        return self.type
    def getCountry(self):
        return self.country
    def printShip(self):
        print("----------------------")
        print("|      Vehicle       |")
        print("----------------------")
        
        self.printVehicle()
        self.move()
        print("Vehicle Type:" + str(self.type))
        print("Vehicle Age: " + str(self.age))
        print("Vehicle Country Manufacture: " + str(self.country))
        print("-----------------------")
        