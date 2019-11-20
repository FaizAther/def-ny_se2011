from Efficiency import Efficiency

class Tracker():
    """docstring for Tracker."""

    CLASSIFY = {'seeder' : 0.5, 'leecher' : 0.35, 'danger' : 0.15}

    def __init__(self):

        self._medicalFacilities = []

    def test():
        print("hello")

    def medicalFacilities(self, medicalFacility):
        self._medicalFacilities.append(medicalFacility)

    def invokeEfficiency(medicalFacility, type, requested):
        blood = Efficiency.getBestBlood(medicalFacility.storage(), type, requested)
        if (medicalFacility.capacity().checkLevels(blood.type())):
            # Impliment in Tracker.py
            findSeeder(medicalFacility, blood.type())

        return blood

    def findSeeder(medicalFacility, type):
        return None

    def __str__(self):
        str = "Medical Facilities"
        for m in self._medicalFacilities:
            str+="\n+++\n"
            str+=m.__str__()
        str+="\n+++"
        return str

if __name__ == "__main__":
    from MedicalFacility import *

    t = Tracker()
    h1 = MedicalFacility("Sydney Children Hospital",
                            "20, High Street, Randwick 2031, Sydney, NSW, AU",
                            1000000)
    t.medicalFacilities(h1)
    h1.addBloodFromParams("2019-11-14", 200, type='AB+')
    h1.addBloodFromParams("2019-11-14", 200, type='AB+')
    h1.addBloodFromParams("2019-11-14", 200, type='AB+')
    h1.addBloodFromParams("2019-11-14", 200, type='AB+')
    h1.addBloodFromParams("2019-11-14", 200, type='AB+')
    h1.addBloodFromParams("2019-11-14", 200, type='AB+')
    h1.addBloodFromParams("2019-11-14", 200, type='AB+')
    h1.addBloodFromParams("2019-11-14", 200, type='AB+')
    h1.addBloodFromParams("2019-11-14", 200, type='AB+')
    h1.addBloodFromParams("2019-11-14", 200, type='AB+')
    h1.addBloodFromParams("2019-11-14", 200, type='AB+')
    h1.addBloodFromParams("2019-11-14", 200, type='AB+')
    h1.addBloodFromParams("2019-11-14", 200, type='AB+')
    h1.addBloodFromParams("2019-11-14", 200, type='AB+')

    h2 = MedicalFacility("Melbourne Children Hospital",
                            "10, Low Street, Richmond 3031, Melboure, VIC, AU",
                            500000)
    h2.addBloodFromParams("2019-11-14", 200, type='AB+')
    t.medicalFacilities(h2)
    print(t)
