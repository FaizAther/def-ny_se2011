

from Blood import *
from Capacity import *
from MedicalFacility import *
from Efficiency import *
from Tracker import *
from Donor import *
from datetime import *


def getInput(cond = lambda x: True, prompt = ">> "):
	while 1:
		command = input(prompt)
		if cond(command): return command

def isDate(date):
	try:
		datetime.strptime(date, '%Y-%m-%d')
		return True
	except ValueError:
		return False

def isNum(n):
	try:
		int(n)
		return True
	except Exception as e:
		return False
		
def isPositive(n): return isNum(n) and int(n) > 0

def isBloodType(b):
	return b in ["O-", "O+", "B-", "B+", "A-", "A+", "AB-", "AB+"]




# Facility Commands
def facilityStatus(f):
	"""Display the status of your facility"""
	print(f._capacity)

def addBlood(f):
	"""Add blood to your facility"""
	# Get blood date
	date = getInput(isDate, "Enter date blood was drawn (YYYY-MM-DD): ")
	# Get blood amount
	amount = getInput(isNum, "Enter amount of blood: ")
	b = Blood(date, int(amount))
	# Get blood type
	type = getInput(isBloodType, "Enter blood type: ")
	b.verify(type)
	# Add blood to facility
	f.addBlood(b)

def removeBlood(f):
	"""Remove blood from your facility"""
	f.displayBlood()
	id = getInput(lambda x:isPositive(x) and int(x) < len(bloodList) and bloodList[int(x)] in f._capacity._inventory, "Enter blood id: ")
	f.removeBlood(bloodList[int(id)])
	

def requestBlood(f):
	"""Request blood to use"""
	btype = getInput(isBloodType, "Enter blood type: ")
	amount = int(getInput(isPositive, "Enter amount: "))
	blood = Tracker().invokeEfficiency(f, btype, amount)
	if type(blood) is not list: blood = [blood]
	if blood:
		if len(blood) > 1:
			print("These blood bags have been allocated to your use:")
		else:
			print("This blood bag has been allocated to your use:")
		print("\n".join(map(str, blood)))
	else:
		print("No blood is available for use")

def checkExpired(f):
	"""Show a list of expired blood bags"""
	bs = f.expiredBlood()
	if bs:
		print("The blood bags with ids %s are expired.\nPlease remove them and type the command 'remove blood' for each of them."%(map(lambda b: b._id, bs)))
	else:
		print("No blood bags are expired")

# Admin Commands
def addFacility():
	"""Add a facility to the system"""
	name = getInput(lambda x: x != 'Admin' and x not in facilityList.keys(), "Enter name of new facility: ")
	capacity = getInput(isPositive, "Enter capacity: ")
	
	MedicalFacility(name, None, int(capacity))
	
	
def adminStatus():
	"""Display a list of facilities"""
	print("Medical Facilities:")
	for m in sorted([*facilityList.values()], key=lambda h: h._capacity.totalBloodAmount(), reverse = True):
		print("\t%s: %s/%s mL"%(m._name, m._capacity.totalBloodAmount(), m._capacity._max))
		
		
def registerDonor(f = None):
	"""Register a donor"""
	name = getInput(str, "Enter donor name: ")
	pc = int(getInput(isPositive, "Enter postcode: "))
	btype = getInput(isBloodType, "Enter blood type: ")

	d = Donor(name, pc, btype)
	d.verify(btype)

def listDonors(f = None):
	"""List all donors"""
	print("\n".join(map(str, donorList)))
	
	
def queryDonor(f = None):
	"""Find donors by blood type"""
	btype = getInput(isBloodType, "Enter blood type: ")
	print("\n".join(map(str, filter(lambda d: d._type == btype, donorList))))
	
def getType(f):
	"""Display all bags of a certain blood type"""
	btype = getInput(isBloodType, "Enter blood type: ")
	bs = [*filter(lambda b: b._type == btype, f._capacity._storage._allBlood)]
	
	print("\n".join(map(str, bs)))
	print("Total:", sum(map(lambda b: b._amount, bs)))
	
def removeExpiredBlood(f):
	"""Removes expired blood"""
	return f.removeExpiredBlood()