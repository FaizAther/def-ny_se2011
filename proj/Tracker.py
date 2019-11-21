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

    def invokeEfficiency(self, medicalFacility, type, requested):
        blood = Efficiency.getBestBlood(medicalFacility.storage(), type, requested)
        if (medicalFacility.capacity().checkLevels(blood.type())):
            # Impliment in Tracker.py
            self.findSeeder(medicalFacility, blood.type())

        return blood

    def findSeeder(self, medicalFacility, type):
        #self._medicalFacilities.remove(medicalFacility)
        for mF in self._medicalFacilities:
            mF.initWeight()
            mF.initDonatable()

        for mF in self._medicalFacilities:
            if mF != medicalFacility:
                mF.weight(mF.typeStoragePerCapacity(type) - CLASSIFY['seeder'])
                mF.donatable(type)
            else:
                mF.weight(None)
                mF.dobatable(None)
        #Sort by most donatable
        ## CHECK THIS
        self._medicalFacilities = self.sortByDonatability(self._medicalFacilities)
        transfer = 0
        for mF in self._medicalFacilities:
            if mF != medicalFacility:
                for b in mF.getTransfer(type):
                    medicalFacility.addBlood(b)

            if (!medicalFacility.capacity().checkLevels(type):
                break

        return transfer

        def sortByDonatability(bList):
            if len(bList) > 1:
                mid = len(bList)//2
                left = bList[:mid]
                right = bList[mid:]

                Efficiency.sortByDonatability(left)
                Efficiency.sortByDonatability(right)

                i = 0
                j = 0
                k = 0
                while i < len(left) and j < len(right):
                    if left[i].getDonatable() < right[j].getDonatable():
                        bList[k] = left[i]
                        i = i + 1
                    else:
                        bList[k] = right[j]
                        j = j + 1
                    k = k + 1

                while i < len(left):
                    bList[k] = left[i]
                    i = i + 1
                    k = k + 1

                while j < len(right):
                    bList[k] = right[j]
                    j = j + 1
                    k = k + 1

            return bList

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
                            5000)
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
                            3000)
    h2.addBloodFromParams("2019-11-14", 200, type='AB+')
    t.medicalFacilities(h2)
    #print(t)
