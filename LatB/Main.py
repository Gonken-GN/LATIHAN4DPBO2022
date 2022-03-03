from vehicle import Vehicle
from Ship import Ship
from Airplane import Airplane
from Persons import Persons
from Job import Job
from Driver import Driver
sukhoi = Airplane()
sukhoi.setAirplane("Jet Fuel", 200, "tempur", 20, 300)
driver1 = Driver()
driver1.setDriver("1144556633", "09/09/2025", "Airplane")
driver1.setPersons("2929400059", "Soran Ibrahim", "Male")
driver1.setJob("3939400649", "PT Gundam Sejahtera", "Pilot")
print("-----------------------")
print("       Driver 1")
driver1.printDriver()
sukhoi.printAirplane()

titanic = Ship()
titanic.setShip("Bunker", 1000, 30, "Cruise Ship", "England")
driver2 = Driver()
driver2.setDriver("13243533", "06/06/2026", "Ship")
driver2.setPersons("292940069", "Lufy Hidayat", "Male")
driver2.setJob("3939400099", "PT Mary Go Sejahtera", "Captain")
print("-----------------------")
print("       Driver 2")
driver2.printDriver()
titanic.printShip()
