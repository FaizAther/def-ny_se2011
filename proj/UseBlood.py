
class UseBlood(object):
    PATIENT = {'ABpos' : ["O-","O+","B-","B+","A-","A+","AB-","AB+"],
    'ABneg' : ["O-","B-","A-","AB-"],
    'Apos' : ["O-","O+","A-","A+"],
    'Aneg' : ["O-","A-"],
    'Bpos' : ["O-","O+","B-","B+"],
    'Bneg' : ["O-","B-"],
    'Opos' : ["O-","O+"],
    'Oneg' : ["O-"]
    }
    # most efficient algorithm to use blood
    def __init__(self, storage, requestedType):

        self._reqType = requestedType
        self._storage = storage

    def storage(self):
        return self._storage

    def storage(self, newStorage):
        self._storage = newStorage

    def getSuitableBloods(self):

        # TODO: check the blood type requested from table get the suitable blood
        type = self._reqType[:-1]
        con = self._reqType[-1]
        name = type
        if con == "+":
            name+="pos"
        elif con == "-":
            name+="neg"
        else:
            print("name error!!!!")
            return

        print("Requested Blood is: {}\nSuitable blood is: {}".format(self._reqType,UseBlood.PATIENT.get(name)))

        return UseBlood.PATIENT.get(name)

    def getTheBlood(self, suitableBloodType):
        daysLeft = 999999
        for bt in suitableBloodType:
            # TODO: find the blood type in the medical facility
            x = self._storage.getBlood(bt) # get the blood list in each Storage
            # if daysLeft > x[0].isExpired():
            #     daysLeft = x[0].isExpired()
            #print(bt)
            print(x)
            # assume the array is sorted(should be verified)
            # check only index 0 of the array
            # look for expired tomorrow
            # look for quantity highest and closest to expiry
        return "blood";

if __name__ == "__main__":
    from Storage import Storage
    s = Storage()
    s.inventory("Pakistan")
    #print(s)
    from Blood import Blood
    #import datetime.datetime.datetime
    b = Blood("2019/10/10", 500)
    b.verify("AB+")
    #print(b)
    s.addBlood(b)
    b1 = Blood("2019/11/01", 500)
    b1.verify("AB-")
    s.addBlood(b1, room = "Pakistan")
    b2 = Blood("2019/09/01", 500)
    b2.verify("AB-")
    s.addBlood(b2, room = "Pakistan")
    c1= UseBlood(s,"AB+")
    x = c1.getSuitableBloods()
    c1.getTheBlood(x)
    #print(UseBlood.ABpos)
    # TODO: use blood that will expired tomorrow or
    # TODO: use blood that has highest quantity with closest to expiry
