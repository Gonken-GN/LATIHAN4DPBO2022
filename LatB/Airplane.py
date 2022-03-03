from vehicle import Vehicle
class Airplane(Vehicle):
    def __init__(self):
        self.type = ""
        self.age = 0
        self.wingslength = 0
    def setAirplane(self, fueltype, maxpasengger, type, age, wingslength):
        self.setVehicle(fueltype, maxpasengger)
        self.boolean(0)
        self.type = type
        self.age = age
        self.wingslength = wingslength
    def getType(self):
        return self.type
    def getAge(self):
        return self.age
    def getWingslength(self):
        return self.wingslength
    
    def printAirplane(self):
        print("----------------------")
        print("|      Vehicle       |")
        print("----------------------")
        self.printVehicle()
        self.move()
        print("Airplane Class: ")
        print("Type        : " + str(self.type))
        print("Age         : " + str(self.age))
        print("Wings Length: " + str(self.wingslength))
        print("-----------------------")
