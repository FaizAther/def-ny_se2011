
# This is the list of blood bags to use as reference when getting blood by id
bloodList = []
def assignId(blood):
    bloodList.append(blood)
    return len(bloodList)-1

class Blood(object):
    """docstring for Blood."""

    def __init__(self, collectionDate, amount):
        self._collectionDate = collectionDate
        self._amount = amount
        self._isVerified = False
        self._type = None
        self._storage = None
        self._id = assignId(self)

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
        return "{}, {}, {}, {}".format(self._collectionDate, self._amount, self._type, self._isVerified)

if __name__ == "__main__":
    import datetime
    b1 = Blood(datetime.datetime.now(), 500)
    b1.verify("B+")
    print(b1)
