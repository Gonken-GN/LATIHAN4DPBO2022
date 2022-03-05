from vehicle import Vehicle
from Ship import Ship
from Airplane import Airplane
from Persons import Persons
from Job import Job
from Driver import Driver
driver1 = Driver()
driver1.setDriver("1144556633", "09/09/2025", "Airplane")
driver1.setPersons("2929400059", "Soran Ibrahim", "Male")
driver1.setJob("3939400649", "PT Gundam Sejahtera", "Pilot")
driver1.printDriver()

driver2 = Driver()
driver2.setDriver("13243533", "06/06/2026", "Ship")
driver2.setPersons("292940069", "Lufy Hidayat", "Male")
driver2.setJob("3939400099", "PT Mary Go Sejahtera", "Captain")
driver2.printDriver()

driver3 = Driver()
driver3.setDriver("1144556644", "10/10/2025", "Airplane")
driver3.setPersons("2929400060", "Sung Jin Woo", "Male")
driver3.setJob("3939400649", "PT Leveling", "Pilot")
driver3.printDriver()

driver4 = Driver()
driver4.setDriver("1144556688", "3/4/2025", "Airplane")
driver4.setPersons("2929400063", "Marina Ismail", "Female")
driver4.setJob("3939400649", "PT Templ", "Pilot")
driver4.printDriver()

driver5 = Driver()
driver5.setDriver("1144556655", "16/6/2025", "Airplane")
driver5.setPersons("2929400061", "Chen Fan", "Male")
driver5.setJob("3939400649", "PT Kultivasi", "Pilot")
driver5.printDriver()

sukhoi = Airplane()
sukhoi.setAirplane("Jet Fuel", 400, "Passenger's Jet", 10, 61, "Boeing 777-200")
sukhoi.printAirplane()

sukhoi2 = Airplane()
sukhoi2.setAirplane("Jet Fuel", 644, "Passengger's Jet", 10, 80, "Airbus A380-800")
sukhoi2.printAirplane()

sukhoi3 = Airplane()
sukhoi3.setAirplane("Jet Fuel", 700, "Passengger's Jet", 10, 68, "Boeing 747-8")
sukhoi3.printAirplane()

sukhoi5 = Airplane()
sukhoi5.setAirplane("Jet Fuel", 50, "Cargo Plane", 10, 68, "Boeing 747 Dreamlifter")
sukhoi5.printAirplane()

sukhoi4 = Airplane()
sukhoi4.setAirplane("Jet Fuel", 50, "Cargo Plane", 10, 68, "Aero Spacelines Super Guppy")
sukhoi4.printAirplane()

titanic = [Ship() for i in range(5)]
titanic[0].setShip("Bunker", 1000, 30, "Cruise Ship", "England", "Titanic")
titanic[1].setShip("Bunker", 6000, 20, "Cruise Ship", "France", "Symphony of the Seas")
titanic[2].setShip("Bunker", 500, 30, "Tanker Ship", "Japan", "Seawise Giant")
titanic[3].setShip("Bunker", 5479, 9, "Cruise Ship", "France", "Harmony of the Seas")
titanic[4].setShip("Bunker", 4500, 9, "War Ship", "United States", "USS Gerald R. Ford")
for i in range(5):
    titanic[i].printShip()