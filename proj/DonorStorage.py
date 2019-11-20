class DonorStorage():

	def __init__(self):
		self._inventory = []
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
					for d in t[k]:
						str+= " -D- "
						str+=d.__str__()
					str+=" -: }"
			str+="\n"
			str+=self._types.__str__()
		return str

	def addDonor(self, donor, **args):

		if args.get('room') == None:
			args['room'] = "Default"

		for r in self._inventory:
			if r.get('name') != args.get("room"):
				continue
			for t in r.get('types'):
				for k in (t.keys()):
					if k == donor.type():
						t.get(k).append(donor)
						self._types[donor.type()]+=1

	def numDonorType(self, bType):
		counter = 0
		counter = self.type(bType)
		return counter

if __name__ == "__main__":
    d = DonorStorage()

    from Donor import Donor

    d1 = Donor("John", 2033, "AB+")
    d1.verify("AB+")
    d.addDonor(d1)

    d2 = Donor("David", 2035, "B+")
    d2.verify("B+")
    d.addDonor(d2)

    #cprint(d)