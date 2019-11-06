class Storage(object):
    def __init__(self):
        self._inventory = []
        self._types = {'O-' : 0, 'O+' : 0, 'B-' : 0, 'B+' : 0, 'A-' : 0, 'A+' : 0, 'AB-' : 0, 'AB+' : 0}
        self.inventory("Default")
#TODO add blood quantity to each type

    def types(self):
        return self._types

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

        return str

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
                        #check expuery and add accordingly
                        t.get(k).append(blood)
                        self._types[blood.type()]+=blood.amount()


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
                        print(b.isExpired())
                        if (b.isExpired() == True):
                            #print ("{} is Expired".format(b))
                            badBlood.append(b)
                            self._types[b.type()]-=b.amount()
                            a.remove(b)
        return badBlood

if __name__ == "__main__":
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
    print(s)
    s.expiration()
    print(s.types())
    print(s)
