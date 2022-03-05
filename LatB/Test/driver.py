# import base 1
from person import person
# import base 2
from job import job


# derived
class driver(person, job):

    # deklrasi atribut privat
    __licenseID = ""
    __activeUntil = ""
    __vehicleType = ""
    __personA = person()
    __jobB = job()

    # membuat constructor
    def __init__(self):
        self.__licenseID = ""
        self.__activeUntil = ""
        self.__vehicleType = ""
        self.__personA = person()
        self.__jobB = job()

    # get set atribut licenseID
    def setID(self, licenseID):
        self.__licenseID = licenseID

    def getID(self):
        return self.__licenseID

    # get set atribut activeUntil
    def setUntil(self, activeUntil):
        self.__activeUntil = activeUntil

    def getUntil(self):
        return self.__activeUntil

    # get set atribut vehicleType
    def setVehicle(self, vehicleType):
        self.__vehicleType = vehicleType

    def getVehicle(self):
        return self.__vehicleType

    # get set object person
    def setPerson(self, personA):
        self.__personA = personA

    def getPerson(self):
        self.__personA

    # get set object job
    def setJob(self, jobB):
        self.__jobB = jobB

    def getJob(self):
        self.__jobB

    # print driver
    def printDriver(self):
        
        print("NIP          : " + str(self.getID()))
        print("Company Name : " + str(self.getUntil()))
        print("Job Position : " + str(self.getPos()))
        print("==================================\n")
