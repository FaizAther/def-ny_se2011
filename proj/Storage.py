class Storage():
    Blood = {'blood':[]}
    Fridge = {'fridge':[Blood]}
    Section = {'section':[Fridge]}
    Room = {'room':[Section]}

    def __init__(self):
        self._inventory = []
        self._allBlood = []
        self._types = {'O-' : 0, 'O+' : 0, 'B-' : 0, 'B+' : 0, 'A-' : 0, 'A+' : 0, 'AB-' : 0, 'AB+' : 0}
        self.inventory("Default")

    def types(self):
        return self._types

    def type(self, bType):
        return self._types[bType]

    def inventory(self, desc):
        self._inventory.append(self.room(desc))

    def room(self, desc):
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
                for k in t.keys():
                    str+="{ "
                    str+=k
                    str+=" :"
                    for b in t[k]:
                        str+= " -b- "
                        str+=b.__str__()
                    str+=" -: }"
            str+="\n"
            str+=self._types.__str__()
        return str


    #Add blood to storage
    #Default unless room name is mentioned
    #Does not add expired blood
    #Add based on closest to expiery first
    def addBlood(self, blood, **args):

        #Does not add if blood is expired
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
                            #checks expiery duration and adds blood
                            if blood.isExpired() <= b.isExpired():
                                j = i
                            i += 1
                        t.get(k).insert(j, blood)
                        self._types[blood.type()]+=blood.amount()
        self._allBlood.append(blood)

    def removeUsedBloodObj(self, blood):
        usedBlood = []
        for r in self._inventory[0].get('types'):
            #for k in r.get('types'):
            for a in r.values():
                for b in a:
                    if b == blood:
                        usedBlood.append(b)
                        self._types[b.type()]-=b.amount()
                        a.remove(b)
        if b in self._allBlood: self._allBlood.remove(b)


    def getTypeArr(self,bloodType):
            for t in self._inventory[0].get('types'):
                for k in t.keys():
                    if k == bloodType:
                        return t.get(k)

    #Loops through rooms
    #Check expiration of blood
    #Removes expired blood from inventory
    #Adds expired blood into badBlood array

    #VERIFICATION
    def expiration(self):
        badBlood = []
        for r in self._inventory:
            #print("R - {}".format(r))
            for t in r.get('types'):
                #print("T - {}".format(t))
                for a in t.values():
                    #print("A - {}".format(a))
                    for b in a:
                        #print("B - {}".format(b))
                        if (b.isExpired() == True):
                            badBlood.append(b)
                            self._types[b.type()]-=b.amount()
                            a.remove(b)
        return badBlood


    def numBagsType(self, bType):
        counter = 0
        for r in self._inventory:
            for t in r.get('types'):
                for a in t.values():
                    for b in a:
                        if(b.type() == bType):
                            counter += 1
        return counter

    def typeQuantity(self, bType):
        counter = 0
        counter = self.type(bType)
        return counter


if __name__ == "__main__":
    s = Storage()

    from Blood import Blood

    b1 = Blood("2019-10-10", 100)
    b1.verify("AB+")
    s.addBlood(b1)

    # Checking Expired blood
    b2 = Blood("2019-09-02", 300)
    b2.verify("AB-")
    s.addBlood(b2)

    b3 = Blood("2019-11-02", 300)
    b3.verify("AB-")
    s.addBlood(b3)

    b4 = Blood("2019-10-31", 500)
    b4.verify("AB-")
    s.addBlood(b4)

    b5 = Blood("2019-11-01", 300)
    b5.verify("AB-")
    s.addBlood(b5)

    b23 = Blood("2019-11-02", 150)
    b23.verify("O-")
    s.addBlood(b23)

    #print(s)