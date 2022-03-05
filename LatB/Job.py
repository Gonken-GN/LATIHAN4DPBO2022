class Job():
    def __init__(self):
        self.nip = ""
        self.companyname = ""
        self.position = ""
    def setJob(self, nip, companyname, position):
        self.nip = nip
        self.companyname = companyname
        self.position = position
    def setNip(self, nip):
        self.nip = nip
    def setCompanyname(self, companyname):
        self.companyname = companyname
    def setPosition(self, position):
        self.position =position
    def getNip(self):
        return self.nip
    def getCompanyname(self):
        return self.companyname
    def getPosition(self):
        return self.position
    def printJob(self):
        
        print("NIP         : " + str(self.nip))
        print("Company Name: " + str(self.companyname))
        print("Position    : " + str(self.position))
        