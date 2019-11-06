class Storage(object):

    def __init__(self):
        self._inventory = []
        self._types = {'O-' : 0, 'O+' : 0, 'B-' : 0, 'B+' : 0, 'A-' : 0, 'A+' : 0, 'AB-' : 0, 'AB+' : 0}
        self.inventory("Default")

#TODO add blood quantity to each type

    def types(self):
        return self._types
    def type(self, bType):
        return self._types[bType]

    def inventory(self, desc):
        self._inventory.append(self.room(desc))

    def room(self, desc):
        #list of blood class
        #Fridge = {fridge:[Blood]}
        #Section = {section:[Fridge]}
        Room = {'name': desc, 'types':[]}
        for t in self._types.keys():
            Blood = {t:[]}
            Room.get('types').append(Blood)
        return Room

    def __str__(self):
        str = "Rooms:\n"
        for r in self._inventory:
            str+=r.get('name')
            str+=" Blood:"
            for t in r.get('types'):
                str+="\n\t"
                str+=t.__str__()
                #for i in r.values():
            str+="\n"
            str+=self._types.__str__()
        return str


    #Add blood to storage
    #Default unless room name is mentioned
    #Does not add expired blood
    #Add based on closest to expiery first

    def addBlood(self, blood, **args):
        if blood.isExpired() == True:
            return
        if args.get('room') == None:
            args['room'] = "Default"
        for r in self._inventory:
            if r.get('name') != args.get("room"):
                continue
            for t in r.get('types'):
                for k in (t.keys()):
                    if k == blood.type():
                        i = 0
                        j = 0
                        for b in t.get(k):
                            if blood.isExpired() <= b.isExpired():
                                print(i)
                                j = i
                            i += 1
                        t.get(k).insert(j, blood)
                        self._types[blood.type()]+=blood.amount()

    def getBlood(self,bloodType):
        # return a list of bloods
        for i in self._inventory:
            return i.get(bloodType)


    #Loops through rooms
    #Check expiration of blood
    #Removes expired blood from inventory
    #Adds expired blod finto badBlood array

    def expiration(self):
        badBlood = []
        for r in self._inventory:
            for t in r.get('types'):
                for a in t.values():
                    for b in a:
                        #print(b.isExpired())
                        if (b.isExpired() == True):
                            #print ("{} is Expired".format(b))
                            badBlood.append(b)
                            self._types[b.type()]-=b.amount()
                            a.remove(b)
                        #print(b)
                    #print(a)
        return badBlood


if __name__ == "__main__":
    s = Storage()
    s.inventory("Pakistan")
    #print(s)

    from Blood import Blood

    # Checking Expiered blood
    b1 = Blood("2019/09/02", 300)
    b1.verify("AB-")
    s.addBlood(b1, room = "Pakistan")

    b2 = Blood("2019/10/10", 100)
    b2.verify("AB+")
    s.addBlood(b2)

    b3 = Blood("2019/11/02", 300)
    b3.verify("AB-")
    s.addBlood(b3, room = "Pakistan")

    #AB- -> b3

    print(s)

    b4 = Blood("2019/10/31", 500)
    b4.verify("AB-")
    s.addBlood(b4, room = "Pakistan")

    print(s)

    #AB- -> b4, b3

    b5 = Blood("2019/11/01", 300)
    b5.verify("AB-")
    s.addBlood(b5, room = "Pakistan")

    #AB- -> b4, b5, b3

    print(s)

    b6 = Blood("2019/11/01", 300)
    b6.verify("O-")
    s.addBlood(b6, room = "Pakistan")

    s.expiration()
    #print(s.types())
    print(s)
