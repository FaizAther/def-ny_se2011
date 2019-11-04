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
        Room = {'name': desc, 'blood':[]}
        for t in Storage.types:
            Blood = {t:[]}
            Room.get('blood').append(Blood)

        return Room

    def __str__(self):
        str = "Rooms:\n"
        for r in self._inventory:
            str+=r.get('name')
            str+=" Blood:"
            for b in r.get('blood'):
                str+="\n\t"
                str+=b.__str__()
            str+="\n"

        return "{}".format(str)



if __name__ == "__main__":
    s = Storage()
    s.inventory("Pakistan")
    print(s)
