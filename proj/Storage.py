class Storage(object):
    types = ["O-", "O+", "B-", "B+", "A-", "A+", "AB-", "AB+"]
    def __init__(self):
        self._inventory = []
        self.inventory("Default")
#TODO add blood quantity to each type


    def inventory(self, desc):
        self._inventory.append(self.room(desc))

    def room(self, desc):
        #list of blood class
        #Fridge = {fridge:[Blood]}
        #Section = {section:[Fridge]}
        Room = {'name': desc, 'types':[]}
        for t in Storage.types:
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

    def addBlood(self, **args):
        if args.get('room') == None:
            args['room'] = "Default"
        for r in self._inventory:
            if r.get('name') != args.get("room"):
                continue
            for t in r.get('types'):
                for k in (t.keys()):
                    if k == args.get("blood").type():
                        #check expuery and add accordingly
                        t.get(k).append(args.get("blood"))


    def expiration(self):
        for room in self._inventory:
            for key in room:
                print(key)


    #Return TRUE if blood is expired
    #Return FALSE if blood is not-expired
    #42 - blood usage limit


    #IF EXPIRED
        #Notify
        #Add blood to expired array
        #Remove blood from storage




if __name__ == "__main__":
    s = Storage()
    s.inventory("Pakistan")
    #print(s)
    from Blood import Blood
    #import datetime.datetime.datetime
    b = Blood("2019/10/10", 500)
    b.verify("AB+")
    print(b)
    s.addBlood(blood = b)
    b1 = Blood("2019/11/01", 500)
    b1.verify("AB-")
    s.addBlood(blood = b1, room = "Pakistan")
    print(s)
