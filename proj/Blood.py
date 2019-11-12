from MedicalFacility import *
import datetime

class Blood():
    """docstring for Blood."""

    def __init__(self, collectionDate, amount):
        self._collectionDate = collectionDate
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

    def __str__(self):
        return "ID: %3s | Collection Date: %10s | Type: %3s | Amount: %5d" % (self._id, self._collectionDate, self._type or "?", self._amount)
        
    def __lt__(self, other):
        return self._collectionDate < other._collectionDate
    
    def fromObject(o):
        b = Blood(datetime.datetime.strptime(o['collectionDate'], '%Y-%m-%d').date(), o['amount'])
        b._isVerified = o['isVerified']
        b._type = o['type']
        if o['storage']: getFacility(o['storage']).addBlood(b)
        
    def toObject(self):
        return {'collectionDate': str(self._collectionDate), 'amount': self._amount, 'isVerified': self._isVerified, 'type': self._type, 'storage': self._storage._facility._name if self._storage else ''}

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
    b1 = Blood(datetime.date.today(), 500)
    b1.verify("B+")
    print(b1)
    print(bloodList)
