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
                #str+=t.__str__()
                for k in t.keys():
                    str+="{ "
                    str+=k
                    str+=" :"
                    for b in t[k]:
                        str+= "-b-"
                        #str+="  "
                        str+=b.__str__()
                    str+="-: }"
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




    #return a list of bloods
    #Return??

    def getTypeArr(self,bloodType):
            #print(self._inventory[1].get('types'))
            for t in self._inventory[0].get('types'):
                #print(t)
                for k in t.keys():
                    if k == bloodType:
                        return t.get(k)
            #return.get(bloodType)


    #Loops through rooms
    #Check expiration of blood
    #Removes expired blood from inventory
    #Adds expired blood into badBlood array

    #VERIFICATION
    def expiration(self):
        badBlood = []
        for r in self._inventory:
            print("R - {}".format(r))
            for t in r.get('types'):
                print("T - {}".format(t))
                for a in t.values():
                    print("A - {}".format(a))
                    for b in a:
                        print("B - {}".format(b))
                        #print(b.isExpired())
                        if (b.isExpired() == True):
                            #print ("{} is Expired".format(b))
                            badBlood.append(b)
                            self._types[b.type()]-=b.amount()
                            a.remove(b)
                        #print(b)
                    #print(a)
        return badBlood


    def numBagsType(self, bType):
        counter = 0
        for r in self._inventory:
            for t in r.get('types'):
                for a in t.values():
                    for b in a:
                        if(b.type() == bType):
                            counter += 1
        #print(counter)
        return counter


    def typeQuantity(self, bType):
        counter = 0
        counter = self.type(bType)
        #print(counter)
        return counter





if __name__ == "__main__":
    s = Storage()
    #s.inventory("Room1")
    #print("Initial Status of Rooms")
    #print(s)
    #print()

    from Blood import Blood

#Adding blood into rooms
#Does not add expiered blood
#Adds based on oldest blood first

    #print("Checks oldest blood first")
    #print("Should not add expired blood")
    #print()

    b1 = Blood("2019/10/10", 100)
    b1.verify("AB+")
    s.addBlood(b1)

    # Checking Expiered blood
    b2 = Blood("2019/09/02", 300)
    b2.verify("AB-")
    s.addBlood(b2)

    #print("Does not add expired blood")
    #print(s)
    #print()

    b3 = Blood("2019/11/02", 300)
    b3.verify("AB-")
    s.addBlood(b3)

    #AB- -> b3
    #print("After adding first set of blood")
    #print(s)
    #print()

    b4 = Blood("2019/10/31", 500)
    b4.verify("AB-")
    s.addBlood(b4)

    #AB- -> b4, b3
    #print("After adding second set of blood")
    #print(s)
    #print()

    b5 = Blood("2019/11/01", 300)
    b5.verify("AB-")
    s.addBlood(b5)

    #AB- -> b4, b5, b3
    #print("After adding third set of blood")
    #print(s)
    #print()

    b23 = Blood("2019/11/02", 150)
    b23.verify("O-")
    s.addBlood(b23)

    #print("NON REMOVED")
    #print(s)
    #print()

    s.expiration()

    #s.removeUsedBloodObj(b23)




#Blood inventory
#Before checking for any expiered blood
    #print("After adding multiple sets of blood")
    #print("Before conducting expiration tests")
    #print(s)
    #print()

    #s.expiration()
    #print(s.expiration())

#After checking for any expired blood
    #print("After conducting expiration tests")
    #print(s)

#blood type - quantity
    #print(s.types())

# s.numBagsType("AB-")

# s.typeQuantity("AB-")
