class Capacity(object):
    """docstring for Capacity."""

    def __init__(self, max):

        types = ["O-", "O+", "B-", "B+", "A-", "A+", "AB-", "AB+"]

        self._max = max
        self._min = []
        self._inventory = []

        for t in types:
            self._min.append({"type":t, "amount":-1})

    def min(self):
        return self._min

    def min(self,type, amount):
        for m in self._min:
            if m.get("type") == type:
                m["amount"] = amount

    def max(self):
        return self._max


    def __str__(self):
        return "{}\n{}\n{}".format(self._max, self._min, self._inventory)

if __name__ == "__main__":
    c1= Capacity(100)
    c1.min("A+", 20)
    c1.min("A-", 0)
    c1.min("B+", 5)
    print(c1)
