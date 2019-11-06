class Efficiency(object):
    PATIENT = {'AB+' : ["O-","O+","B-","B+","A-","A+","AB-","AB+"],
    'AB-' : ["O-","B-","A-","AB-"],
    'A+' : ["O-","O+","A-","A+"],
    'A-' : ["O-","A-"],
    'B+' : ["O-","O+","B-","B+"],
    'B-' : ["O-","B-"],
    'O+' : ["O-","O+"],
    'O-' : ["O-"]
    }

    def findBlood(storage, bType):
        max = 0
        maxT = ""
        for t in Efficiency.PATIENT[bType]:
            print(storage.type(t))
            if max < storage.type(t):
                max = storage.type(t)
                maxT = t
        print(maxT, max)




if __name__== "__main__":
    #print(Efficiency.PATIENT)

    #print(s)

    from Blood import Blood
    from Storage import Storage

    s = Storage()
    s.inventory("Pakistan")

    # Checking Expiered blood
    b1 = Blood("2019/09/02", 300)
    b1.verify("AB-")
    s.addBlood(b1, room = "Pakistan")

    b2 = Blood("2019/10/10", 100)
    b2.verify("AB+")
    s.addBlood(b2)

    b3 = Blood("2019/11/02", 700)
    b3.verify("O-")
    s.addBlood(b3, room = "Pakistan")

    #AB- -> b3


    b4 = Blood("2019/10/31", 500)
    b4.verify("O+")
    s.addBlood(b4, room = "Pakistan")


    #AB- -> b4, b3

    b5 = Blood("2019/11/01", 50)
    b5.verify("A+")
    s.addBlood(b5, room = "Pakistan")

    #AB- -> b4, b5, b3


    b6 = Blood("2019/11/01", 1200)
    b6.verify("B+")
    s.addBlood(b6, room = "Pakistan")

    s.expiration()
    #print(s.types())
    print(s)
    Efficiency.findBlood(s, "A+")
