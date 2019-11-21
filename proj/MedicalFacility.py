from Blood import *
from Capacity import Capacity
import json

def assignFacilityId(facility):
    facilityList[facility._name] = facility
    return len(facilityList)-1


class MedicalFacility():

    # name: str
    # location: (longitude, latitude)
    # capacity: int in the form of mL (remove this later in favour of storage units)
    def __init__(self, name, address, capacity):
        if name in facilityList: raise Exception("Facility with this name already exists")
        if capacity < 0: raise Exception("Capacity for a new Facility can not be negative")

        facilityList[name] = self
        self._name = name
        self._address = address
        self._capacity = Capacity(capacity)
        self._id = assignFacilityId(self)
        self._weight = 0
        self._donatable = 0

    def getTransfer(self, type):
        give, transfered = self._capacity.transfer(type, self._donatable)
        self._donatable -= transfered
        return give

    def typeStoragePerCapacity(self, type):
        return self._capacity.typeStoragePerCapacity()

    def getDonatable(self):
        return self._donatable

    def donatable(self, type):
        self._donatable = self._weight * self._capacity.type(type)

    def getWeight(self):
        return self._weight

    def weight(self, weight):
        self._weight = weight

    def initWeight(self):
        self._weight = 0

    def capacity(self):
        return self._capacity
    def storage(self):
        return self._capacity.storage()

    def name(self):
        return self._name

    def address(self):
        return self._address

    # Send a message to this facility notifying of expired blood
    def notifyExpired(self, bloodId):
        pass

    # Preconditions:
    #    Blood type is known
    #    Amount is positive
    def requestBlood(self, type, amount):
        pass
    # Postconditions:
    #    Blood is moved to location's capacity if not already there
    #    Blood is used and removed from the system

    # Remove blood: This function will be used when a facility uses blood, removes expired blood or transfers blood
    # Preconditions:
    #    Blood is in this location
    def removeBlood(self, blood):
        self._capacity.removeBlood(blood)
    # Postcondition: Blood is removed from this location

    def displayBlood(self):
        self._capacity.displayBlood()

    def addBlood(self, blood):
        self.storage().addBlood(blood)
        blood._storage = self

    def removeExpiredBlood(self):
        return self.storage().expiration()

    def addBloodFromParams(self, date, quantity, **kwargs):
        blood = Blood(date, quantity)
        if (len(kwargs) == 1):
            blood.verify(kwargs['type'])
            #print(blood)
            self.storage().addBlood(blood)

    def __str__(self):
        return "{}\n{}\n{}".format(self._name, self._address, self._capacity)

def getFacility(name): return facilityList[name]

def saveFacilities():
    file = open("facilities.json", 'w')
    fs = {}
    for f in facilityList:
        fs[f] = {'capacity': facilityList[f]._capacity._max}
    file.write(json.dumps(fs))

# This is the list of facilities to use as reference when getting facilities by name
facilityList = {}
try:
    f = open("facilities.json")

    j = f.read()

    fs = json.loads(j)
    for f in fs:
        MedicalFacility(f, None, fs[f]['capacity'])
except Exception as e:
    print(e)



if __name__ == "__main__":
    h1 = MedicalFacility("Sydney Children Hospital",
                            "20, High Street, Randwick 2031,Sydney, NSW, AU",
                            4000)

    h1.addBloodFromParams("2019-11-14", 200, type='AB+')

    h2 = MedicalFacility("Melbourne Children Hospital",
                            "10, High Street, Richmond 3031,Melboure, VIC, AU",
                            5000)

    h2.addBloodFromParams("2019-11-14", 200, type='B+')
    h2.addBloodFromParams("2019-10-14", 300, type='B+')

    #print(h1)
    #print(h2)
