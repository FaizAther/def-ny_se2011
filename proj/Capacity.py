from Storage import Storage

class Capacity():
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

    def typeStoragePerCapacity(self, type):
        return self._storage.type(type) / self.types[type]

    def transfer(self, type, maxTransfer):
        give = []
        amount = 0
        for b in self._storage.getTypeArr(type):
            amount += b.amount()
            if amount > maxTransfer:
                break
            give.append(b)
            self._storage.removeUsedBloodObj(b)
        amount -= b.amount()
        return give



    def type(self, type):
        return self._types[type]

    def storage(self):
        return self._storage

    def max(self):
        return self._max

    def min(self):
        return self._min

    def totalBloodAmount(self):
        return sum(self._storage._types.values())

    # Preconditions:
    #    Blood._isVerified
    #    Blood._amount + self._min.sum < self._max
    #    Blood is not owned by another facility
    def addBlood(self, blood):
        self._storage.addBlood(blood)

    # Postcondition:
    #    Blood is assigned to this capacity
    #    Capacity inventory is sorted by expiry date

    def checkLevels(self, type):
        if self._type[type] < Capacity.MINIMUM_LIMIT * self._storage.type(type):
            return True
        return False

    # Preconditions:
    #    Blood is assigned to this capacity
    def removeBlood(self, blood):
        if blood not in self._inventory: raise Exception("Blood not in inventory")
        self._inventory.remove(blood)
        blood._storage = None
        self._min[blood._type] -= blood._amount
    # Postcondition:
    #    Blood is no longer assigned to a capacity
    #    Blood totals are updated

    def displayBlood(self):
        for b in self._storage._allBlood:
            print("%-3s: %s (%s)"%(b._id, b._amount, b._type) )

    def __str__(self):
        return "\n".join(["Total Capacity: %s"%(self._max),
            "Type totals:",
            "\n".join(map(lambda x:"\t{}: {}".format(x[0], x[1]), sorted(self._storage._types.items(), key=lambda x: -x[1]))),
			"Blood bags:",
            "\n".join(map(str,self._storage._allBlood))
        ])

if __name__ == "__main__":
    c1= Capacity(1000)

    from Blood import Blood

    b1 = Blood("2019-11-01", 200)
    b1.verify("A+")

    b2 = Blood("2019-11-01", 150)
    b2.verify("A-")

    b3 = Blood("2019-11-01", 250)
    b3.verify("B+")

    c1.addBlood(b1)
    c1.addBlood(b2)
    c1.addBlood(b3)
    print(c1)
