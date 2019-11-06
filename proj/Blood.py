
# This is the list of blood bags to use as reference when getting blood by id
bloodList = []
def assignBloodId(blood):
    bloodList.append(blood)
    return len(bloodList)-1

import datetime
from Storage import Storage

class Blood(object):
    """docstring for Blood."""
    import datetime
    def __init__(self, collectionDate, amount):
        self._collectionDate = Blood.datetime.datetime.strptime(collectionDate, "%Y/%m/%d")
        self._amount = amount
        self._isVerified = False
        self._type = None
        self._storage = None
        self._id = assignBloodId(self)

    def collectionDate(self):
        return self._collectionDate

    def amount(self):
        return self._amount

    def isVerified(self):
        return self._isVerified
    
    # Precondition: type is known and valid (one of O, A, B etc.), blood is verified
    def verify(self, type):
        self._type = type
        self._isVerified = True
    # Postcondition: blood is verified and typed

    def type(self):
        return self._type


    def expiration(self):
        for room in self._inventory:
            for key in room:
                print(key)


    #Return TRUE if blood is expired
    #Return FALSE if blood is not-expired
    #42 - blood usage limit
    def isExpired(self, collectionDate):
        currentDate = datetime.datetime.now()
        if((currentDate-collectionDate).days > 42):
            print("Blood is Expired")
            return True
        else:
            return False

    #IF EXPIRED
        #Notify
        #Add blood to expired array
        #Remove blood from storage


    def __str__(self):
        return "{}, {}, {}, {}".format(self._collectionDate, self._amount, self._type, self._isVerified)

if __name__ == "__main__":
    import datetime
    b1 = Blood("2019/11/01", 500)
    b1.verify("B+")
    print(b1)
    #b1.expiration()
