class Capacity(object):
    """docstring for Capacity."""

    def __init__(self, max):

        types = ["O-", "O+", "B-", "B+", "A-", "A+", "AB-", "AB+"]

        self._max = max
        self._min = {}
        self._inventory = []

        for t in types:
            self._min[t] = 0

    def max(self):
        return self._max

    def min(self):
        return self._min

    # Preconditions: 
    #    Blood._isVerified
    #    Blood._amount + self._min[Blood._type] < self._max
    #    Blood is not owned by another facility
    def addBlood(self, blood):
        self._inventory.append(blood)
        self._min[blood._type] += blood._amount
        blood._storage = self
    # Postcondition: blood is assigned to this capacity


    def __str__(self):
        return "{}\n{}\n{}".format(self._max, self._min, list(map(str,self._inventory)))

if __name__ == "__main__":
    c1= Capacity(100)
    import Blood
    import datetime
    
    bag1 = Blood.Blood(datetime.datetime.now(), 20)
    bag1.verify("A+")
    
    bag2 = Blood.Blood(datetime.datetime.now(), 10)
    bag2.verify("A-")
    
    bag3 = Blood.Blood(datetime.datetime.now(), 5)
    bag3.verify("B+")
    
    c1.addBlood(bag1)
    c1.addBlood(bag2)
    c1.addBlood(bag3)
    print(c1)
