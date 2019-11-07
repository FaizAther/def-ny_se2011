class Efficiency(object):

    #Compatible blood groups
    PATIENT = {'AB+' : ["O-","O+","B-","B+","A-","A+","AB-","AB+"],
    'AB-' : ["O-","B-","A-","AB-"],
    'A+' : ["O-","O+","A-","A+"],
    'A-' : ["O-","A-"],
    'B+' : ["O-","O+","B-","B+"],
    'B-' : ["O-","B-"],
    'O+' : ["O-","O+"],
    'O-' : ["O-"]
    }

    BLOOD_RANK = ['AB+', 'AB-', 'A+', 'B+', 'A-', 'B-', 'O+', 'O-']

    REJECTION_CRITERIA = 25

    #Find the compatible blood group with maximum quantity of blood
    #Returns the blood group with maximum quantity
    def findBlood(storage, bType):
        #maximum quantity
        max = 0
        #blood type - maximum quantity
        maxT = ""
        for t in Efficiency.PATIENT[bType]:
            print(storage.type(t))
            if max < storage.type(t):
                max = storage.type(t)
                maxT = t
        print("Highest Amount: {}, {}".format( maxT, max))
        return maxT

    #Returns an array
    #Descending order of blood type
    #Based on quantity
    def amount(storage, bType):
        #
        maxA = []

        for t in Efficiency.PATIENT[bType]:
            #print(storage.type(t))
            i = 0
            j = len(maxA)
            hit = False
            for s in maxA:
                if not hit and storage.type(s) <= storage.type(t):
                    j = i
                    hit = True
                i+=1
            maxA.insert(j, t)
        return maxA

    def need(storage, bTypes):

        return None

    #def 


if __name__== "__main__":
    #print(Efficiency.PATIENT)

    #print(s)

    from Blood import Blood
    from Storage import Storage

    s = Storage()
    s.inventory("Room1")

    # Checking Expiered blood
    b1 = Blood("2019/09/02", 300)
    b1.verify("AB-")
    s.addBlood(b1, room = "Room1")

    b2 = Blood("2019/10/10", 100)
    b2.verify("AB+")
    s.addBlood(b2)

    b3 = Blood("2019/11/02", 700)
    b3.verify("O-")
    s.addBlood(b3, room = "Room1")

    b4 = Blood("2019/10/31", 500)
    b4.verify("O+")
    s.addBlood(b4, room = "Room1")

    b5 = Blood("2019/11/01", 50)
    b5.verify("A+")
    s.addBlood(b5, room = "Room1")

    b6 = Blood("2019/11/01", 1200)
    b6.verify("B+")
    s.addBlood(b6, room = "Room1")


    b7 = Blood("2019/11/06", 400)
    b7.verify("O-")
    s.addBlood(b7, room = "Room1")

    b8 = Blood("2019/11/05", 300)
    b8.verify("O+")
    s.addBlood(b8, room = "Room1")

    b9 = Blood("2019/11/04", 200)
    b9.verify("A-")
    s.addBlood(b9, room = "Room1")

    b10 = Blood("2019/11/03", 100)
    b10.verify("A+")
    s.addBlood(b10, room = "Room1")

    b11 = Blood("2019/11/02", 600)
    b11.verify("B-")
    s.addBlood(b11, room = "Room1")

    b12 = Blood("2019/11/01", 300)
    b12.verify("B+")
    s.addBlood(b12, room = "Room1")

    b13 = Blood("2019/11/01", 250)
    b13.verify("AB-")
    s.addBlood(b13, room = "Room1")

    b14 = Blood("2019/11/02", 150)
    b14.verify("AB+")
    s.addBlood(b14, room = "Room1")


    b15 = Blood("2019/10/31", 750)
    b15.verify("O-")
    s.addBlood(b15, room = "Room1")

    b16 = Blood("2019/10/20", 350)
    b16.verify("O+")
    s.addBlood(b16, room = "Room1")

    b17 = Blood("2019/10/01", 350)
    b17.verify("A-")
    s.addBlood(b17, room = "Room1")

    b18 = Blood("2019/10/21", 200)
    b18.verify("A+")
    s.addBlood(b18, room = "Room1")

    b19 = Blood("2019/10/07", 200)
    b19.verify("B-")
    s.addBlood(b19, room = "Room1")

    b20 = Blood("2019/10/08", 50)
    b20.verify("B+")
    s.addBlood(b20, room = "Room1")

    b21 = Blood("2019/11/01", 150)
    b21.verify("AB-")
    s.addBlood(b21, room = "Room1")

    b22 = Blood("2019/10/09", 120)
    b22.verify("AB+")
    s.addBlood(b22, room = "Room1")


    s.expiration()
    print("Blood Inventory - Quantity")
    print(s.types())
    #print(s)
    print()

    #print("Compatible blood type with the highest quantity")

    #print("Compatible blood for A+")
    #print(Efficiency.findBlood(s, "A+"))
    #print()

    #print("Compatible blood for A-")
    #print(Efficiency.findBlood(s, "A-"))
    #print()

    print("Descending Order bases on blood type quantity")
    #Compatible blood for A+
    print("Compatible blood for AB+")
    print(Efficiency.amount(s, "AB+"))
    print()

    #Compatibvle blood for A-
    #print("Compatible blood for A-")
    #print(Efficiency.amount(s, "A-"))

