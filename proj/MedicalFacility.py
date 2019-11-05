from Capacity import Capacity

# This is the list of facilities to use as reference when getting facilities by name
facilityList = {}

class MedicalFacility():

    # name: str
    # location: (longitude, latitude)
    # capacity: int in the form of mL (remove this later in favour of storage units)
    def __init__(self, name, location, capacity):
        if name in facilityList: raise Exception("Facility with this name already exists")
        if capacity < 0: raise Exception("Capacity for a new Facility can not be negative")
        
        facilityList[name] = self
        self._name = name
        self._location = location
        self._capacity = Capacity(capacity)

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
        pass
    # Postcondition: Blood is removed from this location

    def addBlood(self, blood):
        self._capacity.addBlood(blood)

    def __str__(self):
        return "{}\n{}\n{}".format(self._name, self._location, self._capacity)

if __name__ == "__main__":
    h1 = MedicalFacility("Sydney Children Hospital",
                            (-33.915754, 151.231848),
                            1000000)
    print(h1)
