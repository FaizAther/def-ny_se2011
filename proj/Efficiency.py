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

    BLOOD_RANK = {'AB+' : 1, 'AB-' : 2, 'A+' : 3, 'B+' : 4, 'A-' : 5, 'B-' : 6 ,'O+' : 7, 'O-' : 8}

    CONTRIBUTORS = {'Expiration' : 0.52, 'Wastage' : 0.27, 'TotalQuantity' : -0.15, 'BloodRank' : 0.06}

    EXPIERY_LIMIT = 2

    WASTAGE_LIMIT = .10

    def bloodRank(bType):
        return Efficiency.BLOOD_RANK[bType]

#----------------------------------------------------------------------------

    # # TODO // Change to max/min finder
    # def maxMin(storage, bType):
    #     #maximum quantity
    #     max = 0
    #     #blood type - maximum quantity
    #     maxT = ""
    #     for t in Efficiency.PATIENT[bType]:
    #         print(storage.type(t))
    #         if max < storage.type(t):
    #             max = storage.type(t)
    #             maxT = t
    #     print("Highest Amount: {}, {}".format( maxT, max))
    #     return maxT

#----------------------------------------------------------------------------

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


#----------------------------------------------------------------------------

    def weight(value, min, max, weight):
        if weight > 0: 
            #return weight * ((min - value) / (min - max))
            return weight * ( 1 - ( value - min ) / max )
        else:
            #return (-1 * (weight * ((max - value) / (max - min))))
            return weight * ( ( value - min ) / max )

    #VERIFICATION
    def weightedSum(contributors, array, **options):
        for v in array:
            v.initWeight()

        for c in contributors:
            low, high = Efficiency.values(c, array, options)

            for v in array:
                if type(v).__name__ == 'Blood':
                    if c == 'Expiration':
                        value = v.isExpired()
                    elif c == 'Wastage':
                        value = v.amount() - options['requested']
                    elif c == 'TotalQuantity':
                        value = options['storage'].type(v.type())
                    elif c == 'BloodRank':
                        value = Efficiency.BLOOD_RANK[v.type()]
                    v.weight(Efficiency.weight(value, low, high, contributors[c]))

    #VERIFICATION
    def values(c, array, options):
        if len(array) == 0:
            return r

        if (c == 'Expiration'):
            v = []
            for b in array:
                v.append(b.isExpired())
            return Efficiency.getLowHigh(v)

        elif (c == 'Wastage'):
            v = []
            for b in array:
                v.append(b.amount() - options['requested'])
            return Efficiency.getLowHigh(v)

        elif (c == 'TotalQuantity'):
            v = []
            for b in array:
                v.append(options['storage'].type(b.type()))
            return Efficiency.getLowHigh(v)

        elif (c == 'BloodRank'):
            v = []
            for b in array:
                v.append(Efficiency.BLOOD_RANK[b.type()])
            return Efficiency.getLowHigh(v)

        else:
            print("What?")



    #VERIFICATION
    def getLowHigh(array):
        if len(array) == 0:
            return 0, 0
        else:
            low = array[0]
            high = array[0]
        for a in array:
            #print(a)
            if a < low and a != True:
                low  = a
            elif a > high and a != True:
                high = a

        return low, high


    #VERIFICATION
    def getBestBlood(storage, bType, rQuan):
        #The best blood that can be used
        wantedBlood = []
        bestBloodRank = []

        for b in Efficiency.PATIENT[bType]:
            bList = storage.getTypeArr(b)

            if(Efficiency.getBestList(bList, rQuan) != None):
                wantedBlood.append(Efficiency.getBestList(bList, rQuan))

#MERGE SORT
        # sort by blood type rank
        wantedBlood = Efficiency.sortMByTypeRank(wantedBlood)
        # sort by blood type quantity
        wantedBlood = Efficiency.sortMByTypeQuan(storage, wantedBlood)
        # sort by quantity
        wantedBlood = Efficiency.sortMByQuantity(wantedBlood)
        # sort by expiration
        wantedBlood = Efficiency.sortMByExpiration(wantedBlood)


#BUBBLE SORT
        # sort by blood type rank
        #wantedBlood = Efficiency.sortByTypeRank(wantedBlood)
        # sort by blood type quantity
        #wantedBlood = Efficiency.sortByTypeQuan(storage, wantedBlood)
        # sort by quantity
        #wantedBlood = Efficiency.sortByQuantity(wantedBlood)
        # sort by expiration
        #wantedBlood = Efficiency.sortByExpiration(wantedBlood)


        Efficiency.weightedSum(Efficiency.CONTRIBUTORS, wantedBlood, requested=rQuan, storage=storage)
        Efficiency.sortMByWeight(wantedBlood)

        #Efficiency.sortByWeight(wantedBlood)

        print(wantedBlood)
        print()

        #
        storage.removeUsedBloodObj(wantedBlood[0])

        #returns the best blood suitable
        return wantedBlood[0]


    #Sorts through each list of compatible bloods
    #Returns the best available blood from each list

    #VERIFICATION
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
                if(i.amount() <= (rQuan + (rQuan * Efficiency.WASTAGE_LIMIT)) and i.amount() >= rQuan) or i.isExpired() <= Efficiency.EXPIERY_LIMIT:
                    best.append(i)
                    counter += 1
                #not best suitable criteria
                else:
                    notBest.append(i)
            #no blood is greater than quantity requested
            #should try summing the least two quantities
            else:
                print("Required blood smaller than quantity")


    #MERGE SORT
        # sort by quantity
        best = Efficiency.sortMByQuantity(best)
        # sort by expiration
        best = Efficiency.sortMByExpiration(best)

        # sort by expiration
        notBest = Efficiency.sortMByExpiration(notBest)
        # sort by quantity
        notBest = Efficiency.sortMByQuantity(notBest)

    # #BUBBLE SORT
    #     # sort by quantity
    #     best = Efficiency.sortByQuantity(best)
    #     # sort by expiration
    #     best = Efficiency.sortByExpiration(best)

    #     # sort by expiration
    #     notBest = Efficiency.sortByExpiration(notBest)
    #     # sort by quantity
    #     notBest = Efficiency.sortByQuantity(notBest)


        #no blood matches quantity
        if(counter == 0 and len(notBest) == 0):
            return None
        #does not match best suitable criteria
        elif (counter == 0):
            return notBest[0]
        #best suitable
        else:
            return best[0]

#MERGE SORT

    #Merge Sort based on Quantity
    def sortMByQuantity(bList):
        if len(bList) > 1:
            mid = len(bList)//2
            left = bList[:mid]
            right = bList[mid:]

            Efficiency.sortMByQuantity(left)
            Efficiency.sortMByQuantity(right)

            i = 0
            j = 0
            k = 0
            while i < len(left) and j < len(right):
                if left[i].amount() < right[j].amount():
                    bList[k] = left[i]
                    i = i + 1
                else:
                    bList[k] = right[j]
                    j = j + 1
                k = k + 1

            while i < len(left):
                bList[k] = left[i]
                i = i + 1
                k = k + 1

            while j < len(right):
                bList[k] = right[j]
                j = j + 1
                k = k + 1

        return bList

    #Merge Sort based on Expiration
    def sortMByExpiration(bList):
        if len(bList) > 1:
            mid = len(bList)//2
            left = bList[:mid]
            right = bList[mid:]

            Efficiency.sortMByExpiration(left)
            Efficiency.sortMByExpiration(right)

            i = 0
            j = 0
            k = 0
            while i < len(left) and j < len(right):
                if left[i].isExpired() < right[j].isExpired():
                    bList[k] = left[i]
                    i = i + 1
                else:
                    bList[k] = right[j]
                    j = j + 1
                k = k + 1

            while i < len(left):
                bList[k] = left[i]
                i = i + 1
                k = k + 1

            while j < len(right):
                bList[k] = right[j]
                j = j + 1
                k = k + 1

        return bList

    #Merge Sort based on Blood Weight
    def sortMByWeight(bList):
        if len(bList) > 1:
            mid = len(bList)//2
            left = bList[:mid]
            right = bList[mid:]

            Efficiency.sortMByWeight(left)
            Efficiency.sortMByWeight(right)

            i = 0
            j = 0
            k = 0
            while i < len(left) and j < len(right):
                if left[i].getWeight() < right[j].getWeight():
                    bList[k] = left[i]
                    i = i + 1
                else:
                    bList[k] = right[j]
                    j = j + 1
                k = k + 1

            while i < len(left):
                bList[k] = left[i]
                i = i + 1
                k = k + 1

            while j < len(right):
                bList[k] = right[j]
                j = j + 1
                k = k + 1

        return bList

    #Merge Sort based on blood type quantity
    def sortMByTypeQuan(storage, bList):
        if len(bList) > 1:
            mid = len(bList)//2
            left = bList[:mid]
            right = bList[mid:]

            Efficiency.sortMByTypeQuan(storage, left)
            Efficiency.sortMByTypeQuan(storage, right)

            i = 0
            j = 0
            k = 0
            while i < len(left) and j < len(right):
                if(storage.type(left[i].type()) < storage.type(right[j].type())):
                    bList[k] = left[i]
                    i = i + 1
                else:
                    bList[k] = right[j]
                    j = j + 1
                k = k + 1

            while i < len(left):
                bList[k] = left[i]
                i = i + 1
                k = k + 1

            while j < len(right):
                bList[k] = right[j]
                j = j + 1
                k = k + 1

        return bList

    def sortMByTypeRank(bList):
        if len(bList) > 1:
            mid = len(bList)//2
            left = bList[:mid]
            right = bList[mid:]

            Efficiency.sortMByTypeRank(left)
            Efficiency.sortMByTypeRank(right)

            i = 0
            j = 0
            k = 0
            while i < len(left) and j < len(right):
                if(Efficiency.BLOOD_RANK[left[i].type()] > Efficiency.BLOOD_RANK[right[j].type()]):
                    bList[k] = left[i]
                    i = i + 1
                else:
                    bList[k] = right[j]
                    j = j + 1
                k = k + 1

            while i < len(left):
                bList[k] = left[i]
                i = i + 1
                k = k + 1

            while j < len(right):
                bList[k] = right[j]
                j = j + 1
                k = k + 1

        return bList


#BUBBLE SORT
#-----------------------------------------------------------------------------
    # #sorts based on quantity
    # def sortByQuantity(bList):
    #     n = len(bList)
    #     for i in range(n):
    #         for j in range(0, n-i-1):
    #             if(bList[j].amount() > bList[j+1].amount()):
    #                 bList[j], bList[j+1] = bList[j+1], bList[j]
    #     return bList

    # #sorts based on expiration duration
    # def sortByExpiration(bList):
    #     n = len(bList)
    #     for i in range(n):
    #         for j in range(0, n-i-1):
    #             if(bList[j].isExpired() > bList[j+1].isExpired()):
    #                 bList[j], bList[j+1] = bList[j+1], bList[j]
    #     return bList

    # #sorts based on weight
    # def sortByWeight(bList):
    #     n = len(bList)
    #     for i in range(n):
    #         for j in range(0, n-i-1):
    #             if(bList[j].getWeight() > bList[j+1].getWeight()):
    #                 bList[j], bList[j+1] = bList[j+1], bList[j]
    #     return bList

    # # sort by blood type quantity
    # def sortByTypeQuan(storage, bList):
    #     n= len(bList)
    #     for i in range(n):
    #         for j in range(0, n-i-1):
    #             if(storage.type(bList[j].type()) < storage.type(bList[j+1].type())):
    #                 bList[j], bList[j+1] = bList[j+1], bList[j]
    #     return bList

    # # sort by blood type rank
    # def sortByTypeRank(bList):
    #     n = len(bList)
    #     for i in range(n):
    #         for j in range(0, n-i-1):
    #             if(Efficiency.BLOOD_RANK[bList[j].type()] > Efficiency.BLOOD_RANK[bList[j+1].type()]):
    #                 bList[j], bList[j+1] = bList[j+1], bList[j]
    #     return bList
#-----------------------------------------------------------------------------



if __name__== "__main__":

    print(Efficiency.PATIENT)
    #print(s)

    from Blood import Blood
    from Storage import Storage
    
    s = Storage()
    #s.inventory("Room1")
    #print(s)
    
    
    #b2, b6, b1, b3, b5, b4
    #or
    #b6, b2, b1, b3, b5, b4
    
    # b1 = Blood("2019/09/29", 300)
    # b1.verify("A+")
    # s.addBlood(b1)
    
    # b2 = Blood("2019/09/29", 200)
    # b2.verify("A+")
    # s.addBlood(b2)
    
    # b3 = Blood("2019/09/30", 250)
    # b3.verify("A+")
    # s.addBlood(b3)
    
    # b4 = Blood("2019/10/02", 50)
    # b4.verify("A+")
    # s.addBlood(b4)
    
    # b5 = Blood("2019/10/01", 150)
    # b5.verify("A+")
    # s.addBlood(b5)
    
    # b6 = Blood("2019/09/29", 200)
    # b6.verify("A-")
    # s.addBlood(b6)


    b1 = Blood("2019/10/29", 300)
    b1.verify("A-")
    s.addBlood(b1)
    
    b2 = Blood("2019/10/29", 200)
    b2.verify("A+")
    s.addBlood(b2)
    
    b3 = Blood("2019/10/10", 250)
    b3.verify("O+")
    s.addBlood(b3)
    
    b4 = Blood("2019/10/10", 150)
    b4.verify("O-")
    s.addBlood(b4)
    
    b5 = Blood("2019/10/11", 150)
    b5.verify("A+")
    s.addBlood(b5)
    
    b6 = Blood("2019/10/10", 200)
    b6.verify("A-")
    s.addBlood(b6)
    
    #print(s)
    
    #print("Best blood choice for A+")
    #print(Efficiency.getBestBlood(s, "A+", 100))


    #SET1

    # b7 = Blood("2019/10/02", 300)
    # b7.verify("O-")
    # s.addBlood(b7)

    # b8 = Blood("2019/10/02", 200)
    # b8.verify("O+")
    # s.addBlood(b8)

    # b9 = Blood("2019/10/03", 400)
    # b9.verify("A-")
    # s.addBlood(b9)

    # b10 = Blood("2019/10/04", 100)
    # b10.verify("A+")
    # s.addBlood(b10)

    # b11 = Blood("2019/10/01", 250)
    # b11.verify("B-")
    # s.addBlood(b11)

    # b12 = Blood("2019/10/01", 350)
    # b12.verify("B+")
    # s.addBlood(b12)

    # b13 = Blood("2019/10/06", 450)
    # b13.verify("AB-")
    # s.addBlood(b13)

    # b14 = Blood("2019/10/05", 150)
    # b14.verify("AB+")
    # s.addBlood(b14)


    # #Expired Blood
    # #SET2

    # b15 = Blood("2019/09/02", 300)
    # b15.verify("O-")
    # s.addBlood(b15)

    # b16 = Blood("2019/09/02", 200)
    # b16.verify("O+")
    # s.addBlood(b16)

    # b17 = Blood("2019/09/03", 400)
    # b17.verify("A-")
    # s.addBlood(b17)

    # b18 = Blood("2019/09/04", 100)
    # b18.verify("A+")
    # s.addBlood(b18)

    # b19 = Blood("2019/09/01", 250)
    # b19.verify("B-")
    # s.addBlood(b19)

    # b20 = Blood("2019/09/01", 350)
    # b20.verify("B+")
    # s.addBlood(b20)

    # b21 = Blood("2019/09/06", 450)
    # b21.verify("AB-")
    # s.addBlood(b21)

    # b22 = Blood("2019/08/05", 150)
    # b22.verify("AB+")
    # s.addBlood(b22)


    # #SET3

    # b23 = Blood("2019/11/02", 150)
    # b23.verify("O-")
    # s.addBlood(b23)

    # b24 = Blood("2019/11/02", 300)
    # b24.verify("O+")
    # s.addBlood(b24)

    # b25 = Blood("2019/10/31", 100)
    # b25.verify("A-")
    # s.addBlood(b25)

    # b26 = Blood("2019/11/04", 150)
    # b26.verify("A+")
    # s.addBlood(b26)

    # b27 = Blood("2019/11/01", 350)
    # b27.verify("B-")
    # s.addBlood(b27)

    # b28 = Blood("2019/10/21", 2000)
    # b28.verify("B+")
    # s.addBlood(b28)

    # b29 = Blood("2019/10/26", 350)
    # b29.verify("AB-")
    # s.addBlood(b29)

    # b30 = Blood("2019/10/25", 450)
    # b30.verify("AB+")
    # s.addBlood(b30)


    #Checking Expiration
    #s.expiration()
    print("Blood Inventory - Quantity")
    print(s.types())
    #print(s)
    print()


    #Efficiency.findBlood(s, "A+")

    print("Best blood choice for A-")
    print(Efficiency.getBestBlood(s, "A-", 150))

    # contributors = {'Expiration' : 0.52, 'Wastage' : 0.27, 'TotalQuantity' : -0.15, 'BloodRank' : 0.06}

    # #Efficiency.weightedSum(contributors, [])

    # t = [1, 2, 3, -28, 4, 20, 6, 7, 8, 9]

    # from Blood import Blood
    # b = []
    # b31 = Blood("2019/10/04", 1200)
    # b31.verify("AB+")
    # b.append(b31)
    # b32 = Blood("2019/10/05", 1225)
    # b32.verify("AB-")
    # b.append(b32)
    # b33 = Blood("2019/10/10", 1175)
    # b33.verify("A+")
    # b.append(b33)
    # b34 = Blood("2019/10/02", 1280)
    # b34.verify("A-")
    # b.append(b34)
    # b35 = Blood("2019/10/04", 1300)
    # b35.verify("B+")
    # b.append(b35)
    # b36 = Blood("2019/10/02", 1500)
    # b36.verify("B-")
    # b.append(b36)
    # b36 = Blood("2019/10/03", 1175)
    # b36.verify("O+")
    # b.append(b36)
    # b37 = Blood("2019/10/05", 1200)
    # b37.verify("O-")
    # b.append(b37)
    # #print(b36.isExpired())

    # from Storage import Storage

    # s = Storage()

    # b23 = Blood("2019/11/02", 2500)
    # b23.verify("O-")
    # s.addBlood(b23)

    # b24 = Blood("2019/11/02", 1500)
    # b24.verify("O+")
    # s.addBlood(b24)

    # b25 = Blood("2019/10/31", 800)
    # b25.verify("B-")
    # s.addBlood(b25)

    # b26 = Blood("2019/11/04", 750)
    # b26.verify("B+")
    # s.addBlood(b26)

    # b27 = Blood("2019/11/01", 2700)
    # b27.verify("A-")
    # s.addBlood(b27)

    # b28 = Blood("2019/10/21", 1500)
    # b28.verify("A+")
    # s.addBlood(b28)

    # b29 = Blood("2019/10/26", 3000)
    # b29.verify("AB-")
    # s.addBlood(b29)

    # b30 = Blood("2019/10/25", 2500)
    # b30.verify("AB+")
    # s.addBlood(b30)


    # Efficiency.weightedSum(Efficiency.CONTRIBUTORS, b, requested=1000, storage=s)
    # print(s.types())
    # print()
    # print('requested ', 1000)
    # print() 
    # for b in (Efficiency.sortByWeight(b)):
    #     print(b)
