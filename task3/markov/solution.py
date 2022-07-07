

def zeros_matrix(rows, cols):
    A = []
    for i in range(rows):
        A.append([])
        for j in range(cols):
            A[-1].append(myFrac(0,1))
    return A

def copy_matrix(M):
    rows = len(M)
    cols = len(M[0])
    MC = zeros_matrix(rows, cols)
    for i in range(rows):
        for j in range(rows):
            MC[i][j] = M[i][j]


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
            return str(1)
        return str(self.up)+"/"+str(self.down)
    def __repr__(self):
        if self.up == 0:
            return str(self.up)
        if self.up == self.down:
            return str(1)
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

def defineSubM1(m, firstAbs):
    #assumption they come in cnaonical form
    mQ = []
    mR = []
    #mO = [] no interesa (aun)
    #mI = [] no interesa (aun)
    for vali in m[:firstAbs]:
        mQ.append(vali[:firstAbs])
        mR.append(vali[firstAbs:])
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
#print(myFrac(0,1))
#print(myFrac(1,1)+myFrac(0,1))
#print(myFrac(0,1)+myFrac(1,1))
#print(myFrac(1,1)-myFrac(0,1))
#print(myFrac(0,1)-myFrac(1,1))
#print(myFrac(1,1)*myFrac(0,1))
#print(myFrac(0,1)*myFrac(1,1))
#print(myFrac(1,1)/myFrac(0,1)) #<-- Raise error -->
#print(myFrac(0,1)/myFrac(1,1))
#print(myFrac(1,2)*myFrac(2,1))
#print(myFrac(1,2)*myFrac(1,2).getInverse())

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
    return res, absStates

def printMatrix(m):
    for row in m:
        print(row)

Mown, absStates = prepMatrix3(M)

#printMatrix(Mown)

mQ, mR = defineSubM1(Mown, absStates[0])
#print(mQ)
#print(mR)


def ISubsQ(M):
    nrows = len(M)
    ncols = len(M[0])
    if nrows != ncols:
        return M
    for i, vali in enumerate(M):
        for j, valj in enumerate(vali):
            if (i == j):
                M[i][j] = myFrac(1,1) - valj
    return M


#print(ISubsQ(mQ))
#print(myFrac(0,1) - myFrac(1,1))

def identity(N):
    m = []
    for row in range(0, N):
        temp = []
        for col in range(0, N):
            # Here end is used to stay in same line
            if (row == col):
                temp.append(myFrac(1,1))
            else:
                temp.append(myFrac(0,1))
        m.append(temp)
    return m

def copy_matrix2(m):
    res= []
    for i in m:
        temp = []
        for j in i:
            temp.append(j)
        res.append(temp)
    return res

def gaussInvert(m):
    #this should be square matrix in order to be invertible
    nrows = len(m)
    Im = identity(nrows)
    mres = copy_matrix2(m)
    printMatrix(mres)
    c=0
    print('gauss')
    for i in range(nrows):
        print('<--------- it',i,'c',c,'------------>')
        if c >= nrows: 
            break
        print('val',mres[i][c])
        val = mres[i][c]
        if val.up == 0: continue
        invertedVal = val.getInverse()
        if invertedVal.up < 0:
            invertedVal.up = -invertedVal.up #le mandamos positivo nomas
        pivotRow = [k * invertedVal for k in mres[i]]
        #print('inverted',invertedVal)
        #set the row
        mres[i] = pivotRow
        #add the row to the rest of rows
        
        for j in range(nrows):
            if i != j:
                sumRow = [mres[j][i]*myFrac(-1,1)* k for k in pivotRow]
                print('pivot',pivotRow, 'sumrow',sumRow,'a sumar',mres[j])
                mres[j] =  [x + y for x, y in zip(mres[j], sumRow)]
                
        c+=1
        printMatrix(mres)
        #break
        
    return mres
        

def getIn(m):
    nrows = len(m)
    ncols = len(m)
    if nrows != ncols:
        return m
    Im = identity(nrows)
    #print('Q')
    #printMatrix(m)
    #print('I')
    #printMatrix(Im)
    #print('I - Q')
    iq = ISubsQ(m)
    #printMatrix(iq)
    #print('jiro')
    testM = [[myFrac(2,1), myFrac(1,1)],[myFrac(3,1), myFrac(4,5)]]
    gaussInvert(testM)


getIn(mQ)



            

#print(myFrac(-6,2)+myFrac(3,1))





