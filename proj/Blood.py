class Blood(object):
    """docstring for Blood."""

    def __init__(self, collectionDate, amount):
        self._collectionDate = collectionDate
        self._amount = amount
        self._isVerified = False
        self._type = "N/A"


    def collectionDate(self):
        return self._collectionDate

    def amount(self):
        return self._amount

    def isVerified(self):
        return self._isVerified
    def isVerified(self, isVerified):
        self._isVerified = isVerified

    def type(self):
        return self._type
    def type(self, type):
        self._type = type

    def __str__(self):
        return "{}, {}, {}, {}".format(self._collectionDate, self._amount, self._type, self._isVerified)

if __name__ == "__main__":
    b1 = Blood("10/02/2019", 500)
    b1.isVerified(True)
    b1.type("B+")
    print(b1)
