# Main interface for the Vampire systemss

from Blood import *
from Capacity import *
from MedicalFacility import *
from datetime import *
from InterfaceHelperFunctions import *


print("Welcome to Vampire Systems. Login?")
u = getInput(lambda x: x in facilityList or x == 'Admin', "Type Admin, or one of (" + ', '.join(facilityList.keys()) + "): ")
if u != 'Admin': u = facilityList[u]

# Login

# Admin Commands:
#	Add facility
#	Status

adminCommands = {
	'add facility': addFacility,
	'status': adminStatus,
	'donors': listDonors,
	'register donor': registerDonor,
	'query donor': queryDonor,
}

# Facility Commands:
facilityCommands = {
	'status': facilityStatus,
	'add blood': addBlood,
	'request blood': requestBlood,
	'donors': listDonors,
	'register donor': registerDonor,
	'query donor': queryDonor,
	'type': getType,
	'set capacity': changeCapacity
}


print("Type help for a list of commands")

while 1:
	if u != "Admin": 
		bs = u.removeExpiredBlood()
		if bs:
			print("Expired blood bags were removed:")
			print("\n".join(map(str,bs)))
	command = getInput().lower().strip()
	if command == "help":
		print("Commands are:")
		print("\t%-15s: Display this list of commands"%'help')
		commands = adminCommands if u == 'Admin' else facilityCommands
		for c in commands: print("\t%-15s: %s"%(c, commands[c].__doc__))
		print("\t%-15s: Exit the program"%'exit')
	elif command == "exit":
		break
	elif u == 'Admin':
		if command in adminCommands:
			adminCommands[command]()
	else:
		if command in facilityCommands:
			facilityCommands[command](u)

saveDonors()
saveFacilities()
saveBlood()
print("Thank you for using Vampire Systems")
