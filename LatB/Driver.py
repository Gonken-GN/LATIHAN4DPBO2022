from Persons import Persons
from Job import Job
from vehicle import Vehicle
class Driver(Persons, Job):
    def __init__(self):
        self.lisence = ""
        self.activeuntil = ""
        self.vehicletype = ""
    def setDriver(self, lisence, activeuntil, vehicletype):
        self.lisence = lisence
        self.activeuntil = activeuntil
        self.vehicletype = vehicletype
    def setLisence(self, lisence):
        self.lisence = lisence
    def setActiveUntil(self, activeuntil):
        self.activeuntil = activeuntil
    def setVehicleType(self, vehicletype):
        self.vehicletype =vehicletype
    def getLisence(self):
        return self.lisence
    def getActiveUntil(self):
        return self.activeuntil
    def getVehicleType(self):
        return self.vehicletype
    def printDriver(self):
        print("----------------------")
        print("|       Driver       |")
        print("----------------------")
        self.printPersons()
        self.sleep()
        print("Lisence ID  : " + str(self.lisence))
        print("Active Until: " +  str(self.activeuntil))
        print("Vehicle Type: " + str(self.vehicletype))
        self.printJob()
        