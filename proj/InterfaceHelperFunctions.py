

from Blood import *
from Capacity import *
from MedicalFacility import *
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
	except e:
		return False
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
	b = Blood(datetime.strptime(date, '%Y-%m-%d').date(), int(amount))
	# Get blood type
	type = getInput(isBloodType, "Enter blood type: ")
	b.verify(type)
	# Add blood to facility
	f.addBlood(b)

def removeBlood(f):
	"""Remove blood from your hospital"""
	f.displayBlood()
	id = getInput(isBlood, "Enter blood id: ")


# Admin Commands
def addFacility():
	"""Add a facility to the system"""
	name = getInput(lambda x: x != 'Admin' and x not in facilityList.keys(), "Enter name of new facility: ")
	capacity = getInput(lambda x:isNum(x) and int(x) > 0, "Enter capacity: ")
	
	MedicalFacility(name, None, int(capacity))
	
	
def adminStatus():
	"""Display a list of facilities"""
	print("Medical Facilities:")
	for m in sorted([*facilityList.values()], key=lambda h: h._capacity.totalBloodAmount(), reverse = True):
		print("\t%s: %s/%s mL"%(m._name, m._capacity.totalBloodAmount(), m._capacity._max))