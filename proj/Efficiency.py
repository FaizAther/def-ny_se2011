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


    def weight(value, min, max, weight):
        if weight > 0: 
            #return weight * ((min - value) / (min - max))
            return weight * ( 1 - ( value - min ) / max )
        else:
            #return (-1 * (weight * ((max - value) / (max - min))))
            #preturn -weight * ( ( value - min ) / max )
            return weight * ( ( value - min ) / max )


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

    def values(c, array, options):
        if len(array) == 0:
            return None

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


        Efficiency.weightedSum(Efficiency.CONTRIBUTORS, wantedBlood, requested=rQuan, storage=storage)
        Efficiency.sortMByWeight(wantedBlood)

        #Efficiency.sortByWeight(wantedBlood)

        print(wantedBlood)
        print()
        for b in wantedBlood:
            print(b)

        #
        storage.removeUsedBloodObj(wantedBlood[0])

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
                if left[i].getWeight() > right[j].getWeight():
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
                if(storage.type(left[i].type()) > storage.type(right[j].type())):
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
                if(Efficiency.BLOOD_RANK[left[i].type()] < Efficiency.BLOOD_RANK[right[j].type()]):
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


if __name__== "__main__":

    print(Efficiency.PATIENT)
    #print(s)

    from Blood import Blood
    from Storage import Storage
    
    s = Storage()
    #s.inventory("Room1")
    #print(s)


    b1 = Blood("2019/10/29", 300)
    b1.verify("A-")
    s.addBlood(b1)

    b7 = Blood("2019/11/02", 150)
    b7.verify("A-")
    s.addBlood(b7)

    b8 = Blood("2019/11/01", 150)
    b8.verify("A-")
    s.addBlood(b8)
    
    b9 = Blood("2019/10/21", 160)
    b9.verify("O-")
    s.addBlood(b9)

    b4 = Blood("2019/10/15", 170)
    b4.verify("O-")
    s.addBlood(b4)
    
    b6 = Blood("2019/10/15", 200)
    b6.verify("A-")
    s.addBlood(b6)
    
    #print(s)
    
    #print("Best blood choice for A+")
    #print(Efficiency.getBestBlood(s, "A+", 100))


    #Checking Expiration
    #s.expiration()
    print("Blood Inventory - Quantity")
    print(s.types())
    #print(s)
    print()


    #Efficiency.findBlood(s, "A+")

    print("Best blood choice for A-")
    print(Efficiency.getBestBlood(s, "A-", 150))
