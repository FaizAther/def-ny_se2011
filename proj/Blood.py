from MedicalFacility import *
import datetime
import json

# This is the list of blood bags to use as reference when getting blood by id
bloodList = []

def assignBloodId(blood):
    bloodList.append(blood)
    return len(bloodList)-1


class Blood():
    """docstring for Blood."""
    import datetime

    EXPIRATION_PERIOD = 42

    def __init__(self, collectionDate, amount):
        self._collectionDate = Blood.datetime.datetime.strptime(collectionDate, "%Y-%m-%d").date()
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

    #Expired - True
    #Not Expired - number of days to expire
    def isExpired(self):
        #number of days since collected
        numDays = (datetime.date.today()-self._collectionDate).days
        if(numDays >= Blood.EXPIRATION_PERIOD):
            return True
        else:
            #number of days remaining to expire
            numDaysRemaining = Blood.EXPIRATION_PERIOD - numDays
            return numDaysRemaining



    def __str__(self):
        #return "Blood expiry={}, amount={}".format(self.isExpired(), self._amount)
        #return "(expiry,amount)=({},{})".format(self.isExpired(), self._amount)
        return "ID: %3s | Collection Date: %10s | Type: %3s | Amount: %5d | D2E: %d | Weight: %d " % (self._id, self._collectionDate, self._type or "?", self._amount, self.isExpired(), self._weight)



    def __lt__(self, other):
        return self._collectionDate < other._collectionDate

    def fromObject(o):
        b = Blood(o['collectionDate'], o['amount'])
        b._isVerified = o['isVerified']
        b._type = o['type']
        if o['storage']: getFacility(o['storage']).addBlood(b)

    def toObject(self):
        return {'collectionDate': str(self._collectionDate), 'amount': self._amount, 'isVerified': self._isVerified, 'type': self._type, 'storage': self._storage._name if self._storage else ''}



# This is the list of blood bags to use as reference when getting blood by id
bloodList = []
def assignBloodId(blood):
    bloodList.append(blood)
    return len(bloodList)-1

def saveBlood():
    f = open("blood.json",'w')
    b = map(lambda b: b.toObject(), bloodList)
    f.write(json.dumps([*b]))
    f.close()

try:
	f = open("blood.json")

	j = f.read()

	bs = json.loads(j)
	for b in bs:
	    Blood.fromObject(b)
	f.close()
except Exception as e:
	print(e)

if __name__ == "__main__":

    b1 = Blood("2019-10-01", 500)
    b1.verify("B+")
    print(b1)
    z = b1.isExpired()
    if z:
        print("Expired")
    else:
        print("Days to Expire - {}".format(z))
        print()

        b2 = Blood("2019-09-01", 500)
        b2.verify("B-")
        print(b2)
        z = b2.isExpired()
        if(z == True):
            print("Expired")
        else:
            print("Days to Expire - {}".format(z))
            print()

            b3 = Blood("2019-11-01", 500)
            b3.verify("B-")
            print(b3)
            z = b3.isExpired()
            if(z == True):
                print("Expired")
            else:
                print("Days to Expire - {}".format(z))

    print("\n".join(map(str,bloodList)))
