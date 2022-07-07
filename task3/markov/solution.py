from ast import Raise


class myFrac:
    def __init__(self,up,down):
        if down == 0:
            raise ValueError('Cant divide by 0')
        self.up = up
        self.down = down
    def __add__(self, other):
        if other.up == 0:
            return self
        up = self.up * other.down + other.up * self.down
        do =  self.down * other.down
        return myFrac(up,do)
    def __sub__(self, other):
        if other.up == 0:
            return self
        up = self.up * other.down - other.up * self.down
        do =  self.down * other.down
        return myFrac(up,do)
    def __mul__(self, other):
        if other.up == 0:
            return myFrac(0,1)
        return myFrac(self.up*other.up, self.down*other.down)  
    def __div__(self, other):
        if self.up == 0 and other.up != 0:
            return myFrac(0,1)
        elif other.up == 0:
            raise ValueError('Cant divide by 0')   
        return myFrac(self.up*other.down, self.down*other.up) 
    def __str__(self):
        if self.up == 0:
            return str(self.up)
        if self.up == self.down:
            return str(self.up)
        return str(self.up)+"/"+str(self.down)
    def __repr__(self):
        if self.up == 0:
            return str(self.up)
        if self.up == self.down:
            return str(self.up)
        return str(self.up)+"/"+str(self.down)
    def getInverse(self):
        return myFrac(self.down, self.up)
    def setInverse(self):
        up = self.up
        self.up= self.down
        self.down = up
    def set(self, up, down):
        self.up = up
        self.down = down


def solution(m):
    for i in m:
        print (i)
    return 1

def prepareMatrix(m):
    #dest = {}
    absStates= []
    mults=[]
    for i, vali in enumerate(m):
        rowSum = sum(vali)
        mults.append(rowSum)
        #print(rowSum, vali)
        #for j,valj in enumerate(vali):
        #    dest[(i,j)] = valj != 0   
        if rowSum == 0:
            vali[i] = 1
            absStates.append(i)         
    return m, absStates, mults

def defineSubM1(m, absStates):
    #they come in cnaonical form
    firstAbs=absStates[0]
    mQ = []
    mR = []
    #mO = [] no interesa (aun)
    #mI = [] no interesa (aun)
    for i, vali in enumerate(m[0:firstAbs]):
        mQ.extend(vali[:firstAbs])
        mR.extend(vali[firstAbs:])
    return mQ, mR

def defineSubM2(m):
    #they come in cnaonical form
    mQ = []
    mR = []
    #mO = [] no interesa (aun)
    #mI = [] no interesa (aun)
    for i, vali in enumerate(m):
        rowSum = sum(vali)
        if rowSum == 0:
            break
    #print(i)
    for j, valj in enumerate(m[:i]):
        #print(valj)
        mQ.append(valj[:i])
        mR.append(valj[i:])
    return mQ, mR
        

M = [[0,2,1,0,0],
    [0,0,0,3,4],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]]
#a= solution(M)
#m2, absStates, mults = prepareMatrix(M)

#for kiko in m2:
#    print(kiko)
#print(absStates)
#print(mults)
#print(M)

mq, mr = defineSubM2(M)
#print(mq)
#print(mr)


#print(myFrac(1,0)) # <-- Raise error -->
print(myFrac(0,1))
print(myFrac(1,1)+myFrac(0,1))
print(myFrac(0,1)+myFrac(1,1))
print(myFrac(1,1)-myFrac(0,1))
print(myFrac(0,1)-myFrac(1,1))
print(myFrac(1,1)*myFrac(0,1))
print(myFrac(0,1)*myFrac(1,1))
#print(myFrac(1,1)/myFrac(0,1)) #<-- Raise error -->
print(myFrac(0,1)/myFrac(1,1))

def prepMatrix3(m):
    res = []
    absStates= []
    for i, row in enumerate(m):
        temp=[]
        sumVal = sum(row)
        if sumVal == 0:
            absStates.append(i)
        for item in row:
            if sumVal != 0:
                temp.append(myFrac(item,sumVal))
            else:
                temp.append(myFrac(item,1))
        res.append(temp)
    return res

def printMatrix(m):
    for row in m:
        print(row)

Mown = prepMatrix3(M)
printMatrix(Mown)



