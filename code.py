import random
import math


def Binary_To_Decimal(ent):
    ls = []

    for so in ent:
        sum = 0
        counter99 = len(so) - 1
        counter98 = 0

        while counter99 >-1 :
            sum = sum + (int(so[counter99])) * pow(2 ,counter98)
            counter98 = counter98 + 1
            counter99 = counter99 - 1
        ls.append(sum)

    return ls



def Decimal_To_Binary(entr):

    ls = []


    for xo in entr:
        string = ""
        if xo > 1:

            while True:
                
                v2 = xo % 2
                xo = xo // 2                
                string = string + str(v2)
                
                if xo == 0 or xo == 1:
                    string = string + str(xo)               
                    break


            while True:
                if len(string) == 5:
                    break
                string = string + "0"
            
            ls.append(string[::-1])    

        elif xo == 1:
            string = "00001"
            ls.append(string)

        else:
            string = "00000"
            ls.append(string)


    return ls    




def mutation(entry,mutechance):

    finalMute = []

    for za in entry:
        tmp10 = ""

        for g0 in range(len(za)):
            t0 = random.uniform(0,1)
                
            #print(t0)
            if t0 > mutechance:
                tmp10 = tmp10 + za[g0]
            else:
                if za[g0] == "0":
                    tmp10 = tmp10 + "1"
                else:
                    tmp10 = tmp10 + "0"

        if tmp10 == "11111":
            tmp10 = "11110"            

        finalMute.append(tmp10)

    return finalMute  




populationSize = 4
mutationChance = 0.1
recombChance = 0.7
methodOfRecomb = "3"
maxOfLoop = 5
populationNum = [2, 5, 1, 0]

population = Decimal_To_Binary(populationNum)



count = 0

while count < maxOfLoop:
    matingPool = []
    matingPool2 = []
    actualCount = []
    ftinessList = []
    populationNum = Binary_To_Decimal(population)
    sumFtness = 0
    sumActualcount = 0

    for i in populationNum:
        tmp = (i * i) + (2 + i)
        ftinessList.append(tmp)
        sumFtness = sumFtness + tmp

    averageftness = sumFtness / populationSize

    for j in ftinessList:
        tmp1 = j // averageftness
        actualCount.append(tmp1)

    for z in actualCount:
        sumActualcount=sumActualcount + z

    print(sumActualcount)    


    while sumActualcount < populationSize:
        tmp2 = max(actualCount)
        max0 = max(actualCount) + 1

        for w in range(len(actualCount)):
            if tmp2 == actualCount[w]:
                actualCount[w] = max0
                break
        sumActualcount += 1 

    print(actualCount)



    while sumActualcount > populationSize:
        tmp2 = max(actualCount)
        max1 = max(actualCount) - 1

        for w in range(len(actualCount)):
            if tmp2 == actualCount[w]:
                actualCount[w] = max1
                break
        sumActualcount = sumActualcount - 1


    for t in range(len(actualCount)):
        if actualCount[t] == 0:
            pass
        else:
            tmp3 = actualCount[t]
            print(tmp3)

            while(tmp3 > 0):
                matingPool.append(population[t])
                tmp3 = tmp3 - 1

    random.shuffle(matingPool)
    print(matingPool)


    if methodOfRecomb == "1":
        counter5 = 0

        for g in range(len(matingPool) // 2):
            e0 = random.uniform(0,1)
            #print(e0)
            if e0 < recombChance or e0 == recombChance:
                e1 = random.uniform(1,4)
                e2 = round(e1)
               
                tmp4 = str(matingPool[g + counter5])
                tmp5 = str(matingPool[g + counter5 + 1])
            
                q0 = len(tmp4)
        
                tmp6 = ""
                tmp7 = ""

                counter3 = e2
                counter4 = 0


                while counter4 < e2:
                    tmp6 = tmp6 + tmp4[counter4]
                    tmp7 = tmp7 + tmp5[counter4]
                    counter4 = counter4 + 1

                while counter3 < q0:
                    tmp6 = tmp6 + tmp5[counter3]
                    tmp7 = tmp7 + tmp4[counter3]
                    counter3 = counter3 + 1

                #print(tmp6)
                #print(tmp7)
                matingPool2.append(tmp6)
                matingPool2.append(tmp7)
            else:
                matingPool2.append(matingPool[g + counter5])
                matingPool2.append(matingPool[g + counter5 + 1])

            counter5 = counter5 + 1





    if methodOfRecomb == "2":

        counter5 = 0

        for g in range(len(matingPool) // 2):
            e0 = random.uniform(0,1)
            print(e0)

            if e0 < recombChance or e0 == recombChance:
                e1 = random.uniform(1,4)
                print(e1)
                e2 = round(e1)
                print(e2)

                while True:
                    e4 = random.uniform(1,4)
                    e5 = round(e4)
                    if e5 != e2:
                        break

                minCross = min(e2,e5)
                maxCross = max(e2,e5)
                print('min=', minCross)
                print('max=', maxCross)

                tmp4 = str(matingPool[g + counter5])
                tmp5 = str(matingPool[g + counter5+ 1])
            
                q0 = len(tmp4)
                print(tmp4)
                print(tmp5)

                tmp6=""
                tmp7=""

        
                counter3 = minCross
                counter6 = maxCross
                counter4 = 0
                counter7 = minCross


                while counter4 < minCross:
                    tmp6 = tmp6 + tmp5[counter4]
                    tmp7 = tmp7 + tmp4[counter4]
                    counter4 = counter4 + 1

                while counter3 < maxCross:
                    tmp6 = tmp6 + tmp4[counter3]
                    tmp7 = tmp7 + tmp5[counter3]
                    counter3 = counter3 + 1

                while counter6 < q0:
                    tmp6 = tmp6 + tmp5[counter6]
                    tmp7 = tmp7 + tmp4[counter6]
                    counter6 = counter6 + 1



                print(tmp6)
                print(tmp7)
                matingPool2.append(tmp6)
                matingPool2.append(tmp7)
            else:
                matingPool2.append(matingPool[g + counter5])
                matingPool2.append(matingPool[g + counter5 + 1])

            counter5 = counter5 + 1




    if methodOfRecomb == "3":

        counter5 = 0

        for g in range(len(matingPool) // 2):
            tmp4New = ""
            tmp5New = ""
            tmp4 = str(matingPool[g + counter5])
            tmp5 = str(matingPool[g + counter5 + 1])

            print(tmp4)
            print(tmp5)

            counter5 = counter5 + 1
            counter8 = 0

            while counter8 < len(tmp4):
                rand0 = random.uniform(0,1)
                print(rand0)
                if rand0 < 0.5:
                    tmp4New = tmp4New + tmp4[counter8]
                    tmp5New = tmp5New + tmp5[counter8]
                else:
                    tmp4New = tmp4New + tmp5[counter8]
                    tmp5New = tmp5New + tmp4[counter8]       
                counter8 = counter8 + 1    

            matingPool2.append(tmp4New)
            matingPool2.append(tmp5New)


    print(matingPool2)

    for ch in range(len(matingPool2)):
        if matingPool2[ch] == "11111":
            matingPool2[ch] = "11110"

    mutefinal = []
    mutefinal = mutation(matingPool2 , mutationChance)
    population = []

    for eele in mutefinal:
        population.append(eele)
    count = count+1

print(population)