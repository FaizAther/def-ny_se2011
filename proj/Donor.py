donorList = []

def assignDonorId(donor):
	donorList.append(donor)
	return len(donorList)-1

import datetime

class Donor(object):

	import datetime

	def __init__(self, name, postCode, group):
		self._name = name
		self._postCode = postCode
		self._isVerified = False
		self._group = None
		self._id = assignDonorId(self)


	def name(self):
		return self._name

	def postCode(self):
		return self._postCode

	def isVerified(self):
		return self._isVerified

	def verify(self, group):
		self._group = group
		self._isVerified = True

	def group(self):
		return self._group


if __name__ == "__main__":

	p1 = Donor("John", 2033, "AB+")
	p1.verify("AB+")
	print(p1)

	p2 = Donor("David", 2035, "B+")
	p2.verify("B+")
	print(p2)
