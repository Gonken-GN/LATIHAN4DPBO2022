class Vehicle():
    def __init__(self):
        self.fueltype = ""
        self.maxpasengger = 0
        self.boolean = 0
    def setVehicle(self, fueltype, maxpasengger):
        self.fueltype = fueltype
        self.maxpasengger = maxpasengger
    def setFueltype(self, fueltype):
        self.fueltype = fueltype
    def getFueltype(self):
        return self.fueltype
    def setMaxpassengger(self, maxpasengger):
        self.maxpasengger = maxpasengger
    def getMaxpassengger(self):
        return self.maxpasengger
    def setBoolean(self, boolean):
        self.boolean = boolean
    def getBoolean(self):
        return self.boolean
    def printVehicle(self):
        print("Fuel Type      : " + str(self.fueltype))
        print("Max passenggers: " + str(self.maxpasengger) + " People")
        
    def move(self, nama):
        if self.boolean == 1:
            print("Ship " + nama + " is moving")
        elif self.boolean == 0:
            print("Airship " + nama + " is moving")