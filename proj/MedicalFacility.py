from Capacity import Capacity

# This is the list of blood bags to use as reference when getting blood by id
facilityList = []
def assignFacilityId(facility):
    facilityList.append(facility)
    return len(facilityList)-1


class MedicalFacility(object):

    def __init__(self, name, address, capacity):
        self._name = name
        self._address = address
        self._capacity = Capacity(capacity)
        self._id = assignFacilityId(self)

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
    #    Blood is marked for use
    # Return the blood object
    
    
    # Remove blood: This function will be used when a facility either uses blood or removes expired blood
    # Preconditions:
    #    Blood is in this location
    def removeBlood(self, blood):
        pass
    # Postcondition: Blood is deleted from system

    def __str__(self):
        return "{}\n{}\n{}".format(self._name, self._address, self._capacity)

if __name__ == "__main__":
    h1 = MedicalFacility("Sydney Children Hospital",
                            "20, High Street, Randwick 2031,Sydney, NSW, AU",
                            1000000)
    print(h1)
