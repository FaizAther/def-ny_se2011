# This is the list of blood bags to use as reference when getting blood by id
bloodList = []

def assignBloodId(blood):
    bloodList.append(blood)
    return len(bloodList)-1

import datetime

class Blood(object):
    """docstring for Blood."""
    import datetime

    EXPIRATION_PERIOD = 42

    def __init__(self, collectionDate, amount):
        self._collectionDate = Blood.datetime.datetime.strptime(collectionDate, "%Y/%m/%d")
        self._amount = amount
        self._isVerified = False
        self._type = None
        self._storage = None
        self._id = assignBloodId(self)
        self._weight = 0

    def getWeight(self):
        return self._weight
    def weight(self, weight):
        self._weight += weight
    def initWeight(self):
        self._weight = 0

    def collectionDate(self):
        return self._collectionDate

    def amount(self):
        return self._amount

    def isVerified(self):
        return self._isVerified

    # Precondition: type is known and valid (one of O, A, B etc.), blood is verified
    def verify(self, type):
        if type != None:
            self._type = type
            self._isVerified = True
    # Postcondition: blood is verified and typed

    def type(self):
        return self._type

    #Expiered - True
    #Not Expiered - number of days to expiere
    def isExpired(self):
        #number of days since collected
        numDays = (datetime.datetime.now()-self._collectionDate).days
        if(numDays >= Blood.EXPIRATION_PERIOD):
            return True
        else:
            #number of days remaining to expiere
            numDaysRemaining = Blood.EXPIRATION_PERIOD - numDays
            return numDaysRemaining



    def __str__(self):
        #return "Blood expiry={}, amount={}".format(self.isExpired(), self._amount)
        return "T={}(expiry,amount)=({},{}==>W{})".format(self._type, self.isExpired(), self._amount, self._weight)

if __name__ == "__main__":

    import datetime

    b1 = Blood("2019/10/01", 500)
    b1.verify("B+")
    print(b1)
    z = b1.isExpired()
    if(z == True):
        print("Expired")
    else:
        print("Days to Expiere - {}".format(z))
    print()

    b2 = Blood("2019/09/01", 500)
    b2.verify("B-")
    print(b2)
    z = b2.isExpired()
    if(z == True):
        print("Expired")
    else:
        print("Days to Expiere - {}".format(z))
    print()

    b3 = Blood("2019/11/01", 500)
    b3.verify("B-")
    print(b3)
    z = b3.isExpired()
    if(z == True):
        print("Expired")
    else:
        print("Days to Expiere - {}".format(z))