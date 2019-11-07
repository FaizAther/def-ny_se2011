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

    #return a list of bloods
    def getTypeArr(self,bloodType):
            #print(self._inventory[1].get('types'))
            for t in self._inventory[1].get('types'):
                #print(t)
                for k in t.keys():
                    if k == bloodType:
                        return t.get(k)
            #return.get(bloodType)


    #Loops through rooms
    #Check expiration of blood
    #Removes expired blood from inventory
    #Adds expired blood into badBlood array

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
    s.inventory("Room1")
    print("Initial Status of Rooms")
    print(s)
    print()

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
    s.addBlood(b2, room = "Room1")

    #print("Does not add expired blood")
    #print(s)
    #print()

    b3 = Blood("2019/11/02", 300)
    b3.verify("AB-")
    s.addBlood(b3, room = "Room1")
    
    #AB- -> b3
    #print("After adding first set of blood")
    #print(s)
    #print()

    b4 = Blood("2019/10/31", 500)
    b4.verify("AB-")
    s.addBlood(b4, room = "Room1")

    #AB- -> b4, b3
    #print("After adding second set of blood")
    #print(s)
    #print()

    b5 = Blood("2019/11/01", 300)
    b5.verify("AB-")
    s.addBlood(b5, room = "Room1")

    #AB- -> b4, b5, b3
    #print("After adding third set of blood")
    #print(s)
    #print()


#Adding multiple bloods into inventory
    b6 = Blood("2019/11/01", 300)
    b6.verify("O-")
    s.addBlood(b6, room = "Room1")

    b7 = Blood("2019/11/06", 400)
    b7.verify("O-")
    s.addBlood(b7, room = "Room1")

    b8 = Blood("2019/11/05", 300)
    b8.verify("O+")
    s.addBlood(b8, room = "Room1")

    b9 = Blood("2019/11/04", 200)
    b9.verify("A-")
    s.addBlood(b9, room = "Room1")

    b10 = Blood("2019/11/03", 100)
    b10.verify("A+")
    s.addBlood(b10, room = "Room1")

    #Testing expired blood
    bex1 = Blood("2019/08/03", 100)
    bex1.verify("A+")
    s.addBlood(bex1, room = "Room1")

    b11 = Blood("2019/11/02", 600)
    b11.verify("B-")
    s.addBlood(b11, room = "Room1")

    b12 = Blood("2019/11/01", 300)
    b12.verify("B+")
    s.addBlood(b12, room = "Room1")

    b13 = Blood("2019/11/01", 250)
    b13.verify("AB-")
    s.addBlood(b13, room = "Room1")

    b14 = Blood("2019/11/02", 150)
    b14.verify("AB+")
    s.addBlood(b14, room = "Room1")

    b15 = Blood("2019/10/31", 750)
    b15.verify("O-")
    s.addBlood(b15, room = "Room1")

    b16 = Blood("2019/10/20", 350)
    b16.verify("O+")
    s.addBlood(b16, room = "Room1")

    b17 = Blood("2019/10/01", 350)
    b17.verify("A-")
    s.addBlood(b17, room = "Room1")

    b18 = Blood("2019/10/21", 200)
    b18.verify("A+")
    s.addBlood(b18, room = "Room1")

    b19 = Blood("2019/10/07", 200)
    b19.verify("B-")
    s.addBlood(b19, room = "Room1")

    b20 = Blood("2019/10/08", 50)
    b20.verify("B+")
    s.addBlood(b20, room = "Room1")

    b21 = Blood("2019/11/01", 150)
    b21.verify("AB-")
    s.addBlood(b21, room = "Room1")

    b22 = Blood("2019/10/09", 120)
    b22.verify("AB+")
    s.addBlood(b22, room = "Room1")

#Blood inventory
#Before checking for any expiered blood
    #print("After adding multiple sets of blood")
    #print("Before conducting expiration tests")
    #print(s)
    print()

    s.expiration()
    #print(s.expiration())

#After checking for any expired blood
    #print("After conducting expiration tests")
    print(s)

#blood type - quantity
    #print(s.types())

    print(s.getTypeArr("A+"))
