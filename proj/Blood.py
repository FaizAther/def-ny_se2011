from MedicalFacility import *
import datetime
import json

# This is the list of blood bags to use as reference when getting blood by id
bloodList = []

def assignBloodId(blood):
    bloodList.append(blood)
    return len(bloodList)-1


class Blood():
    import datetime

    EXPIRATION_PERIOD = 42

    def __init__(self, collectionDate, amount):
        self._collectionDate = Blood.datetime.datetime.strptime(collectionDate, "%Y-%m-%d").date()
        self._amount = amount
        self._isVerified = False
        self._type = None
        self._storage = None
        self._id = assignBloodId(self)
        self._score = 0

    def getScore(self):
        return self._score

    def score(self, score):
        self._score += score

    def initScore(self):
        self._score = 0

    def collectionDate(self):
        return self._collectionDate

    def amount(self):
        return self._amount

    def isVerified(self):
        return self._isVerified

    def verify(self, type):
        if type != None:
            self._type = type
            self._isVerified = True

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
            numDaysRemaining = Blood.EXPIRATION_PERIOD - numDays
            return numDaysRemaining

    def __str__(self):
        #return "(expiry,amount)=({},{})".format(self.isExpired(), self._amount)
        #return "T={}(expiry,amount)=({},{}==>W{})".format(self._type, self.isExpired(), self._amount, self._score)
        #return "ID: %3s | Collection Date: %10s | Type: %3s | Amount: %5d | D2E: %d " % (self._id, self._collectionDate, self._type or "?", self._amount, self.isExpired())
        #bloodVal = "ID: {} | Collection Date: {} | Type: {} | Amount: {} | D2E: {} | Weight: {}".format(self._id, self._collectionDate, self._type or "?", self._amount, self.isExpired(), self.getScore())

        bloodVal = "ID: {} | Collection Date: {} | Type: {} | Amount: {} | D2E: {}".format(self._id, self._collectionDate, self._type or "?", self._amount, self.isExpired())
        return bloodVal

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

    b1 = Blood("2019-11-01", 500)
    b1.verify("B+")
    #print(b1)

    b2 = Blood("2019-08-01", 450)
    b2.verify("B-")
    z = b2.isExpired()
    #print(b2)

    b3 = Blood("2019-11-08", 300)
    b3.verify("O-")
    z = b3.isExpired()
    #print(b3)

    print("\n".join(map(str,bloodList)))