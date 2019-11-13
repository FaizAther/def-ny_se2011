from Storage import Storage

class Capacity(object):
    """docstring for Capacity."""

    TYPE_ALGO = 1/36

    MINIMUM_LIMIT = 0.15

    def __init__(self, max):

        self._types = {'AB+' : 0, 'AB-' : 0, 'A+' : 0, 'B+' : 0, 'A-' : 0, 'B-' : 0, 'O+' : 0, 'O-' : 0}

        self._max = max
        #self._min = {}
        self._storage = Storage()
        i = 1
        for t in self._types.keys():
            #self._min[t] = 0
            self._types[t] = round(Capacity.TYPE_ALGO * i * max, 0)
            i+=1

    def storage(self):
        return self._storage

    def max(self):
        return self._max

    def min(self):
        return self._min

    # Preconditions:
    #    Blood._isVerified
    #    Blood._amount + self._min.sum < self._max
    #    Blood is not owned by another facility
    def addBlood(self, blood):
        self._inventory.append(blood)
        self._min[blood._type] += blood._amount
        blood._storage = self
    # Postcondition:
    #    Blood is assigned to this capacity
    #    Capacity inventory is sorted by expiry date

    def checkLevels(self, type):
        if self._type[type] < Capacity.MINIMUM_LIMIT * self._storage.type(type):
            return True
        return False


    def __str__(self):
        return "{}\n{}\n{}".format(self._max, self._types, self._storage.__str__())

if __name__ == "__main__":
    c1= Capacity(100)
    # from Blood import Blood
    # #import datetime.datetime
    #
    # bag1 = Blood("2019/11/01", 20)
    # bag1.verify("A+")
    #
    # bag2 = Blood(, 10)
    # bag2.verify("A-")
    #
    # bag3 = Blood(datetime.datetime.now(), 5)
    # bag3.verify("B+")
    #
    # c1.addBlood(bag1)
    # c1.addBlood(bag2)
    # c1.addBlood(bag3)
    print(c1)
