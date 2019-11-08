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

    # def findBlood(storage, bType):
    #     #maximum quantity
    #     max = 0
    #     #blood type - maximum quantity
    #     maxT = ""
    #     for t in Efficiency.PATIENT[bType]:
    #         #print(storage.type(t))
    #         if max < storage.type(t):
    #             max = storage.type(t)
    #             maxT = t
    #     #print("Highest Amount: {}, {}".format( maxT, max))
    #     return maxT


    #Returns an array
    #Descending order of blood type
    #Based on quantity

    # def amount(storage, bType):
    #     #descending order array based on quantity
    #     maxA = []

    #     for t in Efficiency.PATIENT[bType]:
    #         #print(storage.type(t))
    #         i = 0
    #         j = len(maxA)
    #         hit = False
    #         for s in maxA:
    #             if not hit and storage.type(s) <= storage.type(t):
    #                 j = i
    #                 hit = True
    #             i+=1
    #         maxA.insert(j, t)
    #     return maxA


    def getBestBlood(storage, bType, rQuan):
        #The best blood that can be used
        wantedBlood = []

        for b in Efficiency.PATIENT[bType]:
            bList = storage.getTypeArr(b)

            if(Efficiency.getBestList(bList, rQuan) != None):
                wantedBlood.append(Efficiency.getBestList(bList, rQuan))

        #print("Wanted Blood: {}".format(wantedBlood))

        # sort by quantity
        #wantedBlood = sortByQuantity(wantedBlood)

        n = len(wantedBlood)
        for i in range(n):
            for j in range(0, n-i-1):
                if(wantedBlood[j].amount() > wantedBlood[j+1].amount()):
                    wantedBlood[j], wantedBlood[j+1] = wantedBlood[j+1], wantedBlood[j]

        # sort by expiration
        #wantedBlood = sortByExpiration(wantedBlood)

        n = len(wantedBlood)
        for i in range(n):
            for j in range(0, n-i-1):
                if(wantedBlood[j].isExpired() > wantedBlood[j+1].isExpired()):
                    wantedBlood[j], wantedBlood[j+1] = wantedBlood[j+1], wantedBlood[j]

        #returns the best blood suitable
        return wantedBlood[0]


    #Sorts through each list of compatible bloods
    #Returns the best available blood from each list

    def getBestList(bList, rQuan):

        #bloods that do not match best suitable criteria
        notBest = []

        #bloods that matches best suitable criteria
        best = []

        counter = 0

        for i in bList:
            #Cehcks - Bag quantity > requested quantity
            if(i.amount() >= rQuan):
                #checking best suitable criteria
                if(i.amount() <= (rQuan + (rQuan*.10)) and i.amount() >= rQuan) or i.isExpired() <=2:
                    best.append(i)
                    counter += 1
                #not best suitable criteria
                else:
                    notBest.append(i)
            #no blood is greater than quantity requested
            #should try summing the least two quantities
            else:
                print("Required blood smaller than quantity")


        # sort by quantity
        #best = sortByQuantity(best)
        n = len(best)
        for i in range(n):
            for j in range(0, n-i-1):
                if(best[j].amount() > best[j+1].amount()):
                    best[j], best[j+1] = best[j+1], best[j]

        # sort by expiration
        #best = sortByExpiration(best)
        n = len(best)
        for i in range(n):
            for j in range(0, n-i-1):
                if(best[j].isExpired() > best[j+1].isExpired()):
                    best[j], best[j+1] = best[j+1], best[j]

        # sort by expiration
        #notBest = sortByExpiration(notBest)
        n = len(notBest)
        for i in range(n):
            for j in range(0, n-i-1):
                if(notBest[j].isExpired() > notBest[j+1].isExpired()):
                    notBest[j], notBest[j+1] = notBest[j+1], notBest[j]

        # sort by quantity
        #notBest = sortByQuantity(notBest)
        n = len(notBest)
        for i in range(n):
            for j in range(0, n-i-1):
                if(notBest[j].amount() > notBest[j+1].amount()):
                    notBest[j], notBest[j+1] = notBest[j+1], notBest[j]


        #no blood matches quantity
        if(counter == 0 and len(notBest) == 0):
            return None
        #does not match best suitable criteria
        elif (counter == 0):
            return notBest[0]
        #best suitable
        else:
            return best[0]


    #sorts based on quantity

    # def sortByQuantity(bList):
    #     n = len(bList)
    #     for i in range(n):
    #         for j in range(0, n-i-1):
    #             if(bList[j].amount() > bList[j+1].amount()):
    #                 bList[j], bList[j+1] = bList[j+1], bList[j]

    #     return bList


    #sorts based on expiration duration

    # def sortByExpiration(bList):
    #     n = len(bList)
    #     for i in range(n):
    #         for j in range(0, n-i-1):
    #             if(bList[j].isExpired() > bList[j+1].isExpired()):
    #                 bList[j], bList[j+1] = bList[j+1], bList[j]

    #     return bList



if __name__== "__main__":

    #print(Efficiency.PATIENT)
    #print(s)

    from Blood import Blood
    from Storage import Storage

    s = Storage()
    s.inventory("Room1")
    #print(s)


    #b2, b1, b3, b5, b4
    b1 = Blood("2019/09/29", 300)
    b1.verify("A+")
    s.addBlood(b1, room = "Room1")

    b2 = Blood("2019/09/29", 200)
    b2.verify("A+")
    s.addBlood(b2, room = "Room1")

    b3 = Blood("2019/09/30", 250)
    b3.verify("A+")
    s.addBlood(b3, room = "Room1")

    b4 = Blood("2019/10/02", 50)
    b4.verify("A+")
    s.addBlood(b4, room = "Room1")

    b5 = Blood("2019/10/01", 150)
    b5.verify("A+")
    s.addBlood(b5, room = "Room1")

    b6 = Blood("2019/09/29", 100)
    b6.verify("A-")
    s.addBlood(b6, room = "Room1")

    #print(s)

    #print("Best blood choice for A+")
    #print(Efficiency.getBestBlood(s, "A+", 100))


    # b7 = Blood("2019/10/02", 300)
    # b7.verify("O-")
    # s.addBlood(b7, room = "Room1")

    # b8 = Blood("2019/10/02", 200)
    # b8.verify("O+")
    # s.addBlood(b8, room = "Room1")

    # b9 = Blood("2019/10/03", 400)
    # b9.verify("A-")
    # s.addBlood(b9, room = "Room1")

    # b10 = Blood("2019/10/04", 100)
    # b10.verify("A+")
    # s.addBlood(b10, room = "Room1")

    # b11 = Blood("2019/10/01", 250)
    # b11.verify("B-")
    # s.addBlood(b11, room = "Room1")

    # b12 = Blood("2019/10/01", 350)
    # b12.verify("B+")
    # s.addBlood(b12, room = "Room1")

    # b13 = Blood("2019/10/06", 450)
    # b13.verify("AB-")
    # s.addBlood(b13, room = "Room1")

    # b14 = Blood("2019/10/05", 150)
    # b14.verify("AB+")
    # s.addBlood(b14, room = "Room1")

    # #Expired Blood
    # b15 = Blood("2019/09/02", 300)
    # b15.verify("O-")
    # s.addBlood(b15, room = "Room1")

    # b16 = Blood("2019/09/02", 200)
    # b16.verify("O+")
    # s.addBlood(b16, room = "Room1")

    # b17 = Blood("2019/09/03", 400)
    # b17.verify("A-")
    # s.addBlood(b17, room = "Room1")

    # b18 = Blood("2019/09/04", 100)
    # b18.verify("A+")
    # s.addBlood(b18, room = "Room1")

    # b19 = Blood("2019/09/01", 250)
    # b19.verify("B-")
    # s.addBlood(b19, room = "Room1")

    # b20 = Blood("2019/09/01", 350)
    # b20.verify("B+")
    # s.addBlood(b20, room = "Room1")

    # b21 = Blood("2019/09/06", 450)
    # b21.verify("AB-")
    # s.addBlood(b21, room = "Room1")

    # b22 = Blood("2019/08/05", 150)
    # b22.verify("AB+")
    # s.addBlood(b22, room = "Room1")


    # b23 = Blood("2019/11/02", 150)
    # b23.verify("O-")
    # s.addBlood(b23, room = "Room1")

    # b24 = Blood("2019/11/02", 300)
    # b24.verify("O+")
    # s.addBlood(b24, room = "Room1")

    # b25 = Blood("2019/10/31", 100)
    # b25.verify("A-")
    # s.addBlood(b25, room = "Room1")

    # b26 = Blood("2019/11/04", 150)
    # b26.verify("A+")
    # s.addBlood(b26, room = "Room1")

    # b27 = Blood("2019/11/01", 350)
    # b27.verify("B-")
    # s.addBlood(b27, room = "Room1")

    # b28 = Blood("2019/10/21", 2000)
    # b28.verify("B+")
    # s.addBlood(b28, room = "Room1")

    # b29 = Blood("2019/10/26", 350)
    # b29.verify("AB-")
    # s.addBlood(b29, room = "Room1")

    # b30 = Blood("2019/10/25", 450)
    # b30.verify("AB+")
    # s.addBlood(b30, room = "Room1")


    #Checking Expiration
    s.expiration()
    #print("Blood Inventory - Quantity")
    #print(s.types())
    #print(s)
    #print()

    #print("Best blood choice for A-")
    #print(Efficiency.getBestBlood(s, "A-", 150))
