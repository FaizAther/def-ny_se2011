
from Blood import *
from Capacity import *
from MedicalFacility import *
from datetime import *


# Create a generic facility
m1 = MedicalFacility("Hospital",
						(-33.915754, 151.231848),
						1000000)

bag1 = Blood(date.today(), 20)
bag1.verify("A+")

bag2 = Blood(date.today(), 10)
bag2.verify("A-")

bag3 = Blood(date.today(), 5)
bag3.verify("B+")

m1.addBlood(bag1)
m1.addBlood(bag2)
m1.addBlood(bag3)

print("Welcome to Vampire Systems. Login?")
while 1:
	u = input("Type one of (" + ','.join(facilityList.keys()) + "): ")

	if u in facilityList: break 

# Login

# Commands:
#	Add blood
#	Remove blood
#	Request Blood
#	Query Blood
#	Check messages for expired blood

print("Type help for a list of commands")

while 1:
	command = input(">> ").lower()
	if command == "help":
		print("Commands are: 'status', 'add blood', 'remove blood', 'use blood', 'check expired', 'exit'")
	elif command == "status":
		print(m1._capacity)
	elif command == "add blood":
		# Get blood amount
		# Get blood type
		# Add blood to facility
		pass
	elif command == "remove blood":
		# Get blood id
		# Call remove blood
		pass
	elif command == "use blood":
		# Get blood amount
		# Get blood type
		# Call use blood function
		pass
	elif command == "check expired":
		# Print out any blood bags that are expired
		pass
	elif command == "exit":
		break
		
print("Thank you for using Vampire Systems")
	