from time import sleep


class Persons():
    def __init__(self):
        self.nik = ""
        self.name = ""
        self.gender = ""
    def setPersons(self, nik, name, gender):
        self.nik = nik
        self.name = name
        self.gender = gender
    def setNik(self, nik):
        self.nik = nik
    def setName(self, name):
        self.name = name
    def setGender(self, gender):
        self.gender = gender
    def getNik(self):
        return self.gender
    def getName(self):
        return self.name
    def getGender(self):
        return self.gender
    def printPersons(self):
        print("NIK         : " + str(self.nik))
        print("Name        : " + str(self.name))
        print("Gender      : " + str(self.gender))

    def sleep(self):
        print(str(self.name) + " isn't sleeping")