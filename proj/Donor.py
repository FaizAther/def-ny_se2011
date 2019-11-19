donorList = []

def assignDonorId(donor):
	donorList.append(donor)
	return len(donorList)-1

import datetime

class Donor():

	import datetime

	def __init__(self, name, postCode, type):
		self._name = name
		self._postCode = postCode
		self._isVerified = False
		self._type = None
		self._id = assignDonorId(self)


	def name(self):
		return self._name

	def postCode(self):
		return self._postCode

	def isVerified(self):
		return self._isVerified

	def verify(self, type):
		self._type = type
		self._isVerified = True

	def type(self):
		return self._type
		
	def __str__(self):
		return "ID: %3s | Name: %15s | Type: %3s" % (self._id, self._name, self._type or "?")


if __name__ == "__main__":

	p1 = Donor("John", 2033, "AB+")
	p1.verify("AB+")
	print(p1)

	p2 = Donor("David", 2035, "B+")
	p2.verify("B+")
	print(p2)
