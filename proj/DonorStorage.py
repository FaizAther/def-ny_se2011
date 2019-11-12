class DonorStorage(object):

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
				str+=t.__str__()
				#for i in r.values():
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
					if k == donor.group():
						t.get(k).append(donor)
						self._types[donor.group()]+=1


	def numDonorType(self, bType):
		counter = 0
		counter = self.type(bType)
		#print(counter)
		return counter



if __name__ == "__main__":
    d = DonorStorage()
    #print(d)

    from Donor import Donor

    d1 = Donor("John", 2033, "AB+")
    d1.verify("AB+")
    d.addDonor(d1)

    print(d)

    d.numDonorType("AB+")