#from Storage import Storage
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
        return storage

    def storage(self, newStorage):
        self._storage = newStorage

    def getSuitableBloods(self):

        # TODO: check the blood type requested from table get the suitable blood
        type = self._reqType[0]
        con = self._reqType[1]
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
        for b in suitableBloodType:
            # TODO: find the blood type in the medical facility
            x = storage().getBlood(b)
            print(b)
            # check only index 0 of the array
            # look for expired tomorrow
            # look for quantity highest and closest to expiry
        return "blood";

if __name__ == "__main__":
    c1= UseBlood("O+")
    x = c1.getSuitableBloods()
    c1.getTheBlood(x)
    #print(UseBlood.ABpos)
    # TODO: use blood that will expired tomorrow or
    # TODO: use blood that has highest quantity with closest to expiry
