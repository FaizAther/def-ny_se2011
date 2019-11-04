from Capacity import Capacity

class MedicalFacility(object):


    def __init__(self, name, address, capacity):
        self._name = name
        self._address = address
        self._capacity = Capacity(capacity)

    def name(self):
        return self._name

    def address(self):
        return self._address

    def __str__(self):
        return "{}\n{}\n{}".format(self._name, self._address, self._capacity)

if __name__ == "__main__":
    h1 = MedicalFacility("Sydney Children Hospital",
                            "20, High Street, Randwick 2031,Sydney, NSW, AU",
                            1000000)
    print(h1)
