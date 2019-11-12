class Capacity():

    def __init__(self, max, facility):

        self._types = ["O-", "O+", "B-", "B+", "A-", "A+", "AB-", "AB+"]

        self._max = max
        self._min = {}
        self._inventory = []
        self._facility = facility

        for t in self._types:
            self._min[t] = 0

    def max(self):
        return self._max

    def min(self):
        return self._min
        
    def totalBloodAmount(self):
        return sum(self._min.values())

    # Preconditions: 
    #    Blood._isVerified
    #    Blood._amount + self._min.sum < self._max
    #    Blood is not owned by another facility
    def addBlood(self, blood):
        if self.totalBloodAmount() + blood._amount > self._max: raise Exception("Blood capacity exceeds max capacity")
        if blood._storage: raise Exception("Blood is already assigned to a facility")
        self._inventory.append(blood)
        sorted(self._inventory)            # Note: dafny would be inserting this blood into the correct place
        self._min[blood._type] += blood._amount
        blood._storage = self
    # Postcondition: 
    #    Blood is now assigned to this capacity
    #    Capacity inventory is sorted by expiry date

    # Preconditions:
    #    Blood is assigned to this capacity
    def removeBlood(self, blood):
        pass
    # Postcondition: Blood is no longer assigned to a capacity

    def displayBlood(self):
        for b in self._inventory:
            print("%-3s: %s (%s)"%(b._id, b._amount, b._type) )

    def __str__(self):
        tots = 0
        for t in self._types:
            pass
        
        return "Total Capacity: %s\n"%(self._max) + "Type totals: {}\n{}".format(self._min, "\n".join(map(str,self._inventory)))

if __name__ == "__main__":
    c1 = Capacity(100, None)
    from Blood import Blood
    from datetime import date
    
    bag1 = Blood(date.today(), 20)
    bag1.verify("A+")
    
    bag2 = Blood(date.today(), 10)
    bag2.verify("A-")
    
    bag3 = Blood(date.today(), 5)
    bag3.verify("B+")
    
    c1.addBlood(bag1)
    c1.addBlood(bag2)
    c1.addBlood(bag3)
    print(c1)
