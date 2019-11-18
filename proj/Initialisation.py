# Create data for a set of generic facilities

from Blood import *
from Capacity import *
from MedicalFacility import *
from datetime import *
from InterfaceHelperFunctions import *

# Reset lists
facilityList.clear()
bloodList.clear()
today = date.today().strftime("%Y-%m-%d")

# Create a generic facility
m1 = MedicalFacility("Hospital1", None, 200000)

# Add some blood
bag1 = Blood(today, 400)
bag1.verify("A+")

bag2 = Blood(today, 300)
bag2.verify("A-")

bag3 = Blood(today, 500)
bag3.verify("B+")

m1.addBlood(bag1)
m1.addBlood(bag2)
m1.addBlood(bag3)

# Create second facility
m2 = MedicalFacility("Hospital2", None, 50000)

# Add some blood
bag1 = Blood(today, 250)
bag1.verify("O-")

bag2 = Blood(today, 450)
bag2.verify("AB+")

bag3 = Blood(today, 350)
bag3.verify("B-")

m2.addBlood(bag1)
m2.addBlood(bag2)
m2.addBlood(bag3)


# Save to file
saveFacilities()
saveBlood()