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
def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x
class myFrac:
    def __init__(self,up,down):
        if down == 0:
            raise ValueError('Cant divide by 0')
        self.up = up
        self.down = down
    def __add__(self, other):
        if other.up == 0 or other  == 0:
            return self
        up = self.up * other.down + other.up * self.down
        do =  self.down * other.down
        if up == do :return myFrac(1,1)
        return myFrac(up,do)
    def __radd__(self, other):
        if other  == 0:
            return self
        return self.__add__(other)
    def __sub__(self, other):
        if other.up == 0:
            return self
        up = self.up * other.down - other.up * self.down
        do =  self.down * other.down
        if up == do :return myFrac(1,1)
        return myFrac(up,do)
    def __mul__(self, other):
        if other.up == 0:
            return myFrac(0,1)
        up = self.up*other.up
        do = self.down*other.down
        if up == do :return myFrac(1,1)
        return myFrac(up,do)  
    def __div__(self, other):
        if self.up == 0 and other.up != 0:
            return myFrac(0,1)
        elif other.up == 0:
            raise ValueError('Cant divide by 0')
        up = self.up*other.down
        do = self.down*other.up
        if up == do :return myFrac(1,1)   
        return myFrac(up, do) 
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
    def __neg__(self):
        return myFrac(-1 * self.up,self.down)
    def getInverse(self):
        return myFrac(self.down, self.up)
    def setInverse(self):
        up = self.up
        self.up= self.down
        self.down = up
    def set(self, up, down):
        self.up = up
        self.down = down
    def simplySelf(self):
        gcdd = gcd(self.up, self.down)
        self.up = self.up / gcdd
        self.down = self.down / gcdd
    def getsimplify(self):
        gcdd = gcd(self.up, self.down)
        return myFrac(self.up / gcdd, self.down / gcdd)
def defineSubM1(m, firstAbs):
    mQ = []
    mR = []
    for vali in m[:firstAbs]:
        mQ.append(vali[:firstAbs])
        mR.append(vali[firstAbs:])
    return mQ, mR
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
def ISubsQ(M):
    nrows = len(M)
    ncols = len(M[0])
    if nrows != ncols:
        return M
    for i, vali in enumerate(M):
        for j, valj in enumerate(vali):
            if (i == j):
                M[i][j] = myFrac(1,1) - valj
            else:
                M[i][j] = - valj  
    return M
def gaussInvert(m):
    #this should be square matrix in order to be invertible
    nrows = len(m)
    extendedM = []
    for el in range(nrows):
        temp = m[el]
        for kel in range(nrows):
            I = myFrac(0,1)
            if kel == el:
                I = myFrac(1,1)
            temp.append(I)
        extendedM.append(temp)
    for col in range(nrows):
        val = extendedM[col][col]
        pivot_idx = col
        if val.up != 0: pass 
        else: #take the first not null and move to first pos
            for j in range(col,nrows):
                if (j > col):
                    if (extendedM[j][col] != 0):
                        pivot_idx=j
                        break   
        if pivot_idx != col:
            #intercharge cc rows with pivot pos so we can have pivots in 0,0; 1,1; 2,2;... and so
            pivot = extendedM[pivot_idx]
            cc_row = extendedM[col]
            extendedM[col] = pivot
            extendedM[pivot_idx] = cc_row
        #now pivot is on CC
        val = extendedM[col][col]
        if val != 1:
            #resize pivot to 1
            invertedVal = val.getInverse()
            extendedM[col] = [k * invertedVal for k in extendedM[col]]
        #sum to down
        for j in range(nrows):
            if( j != col):
                sumRow = [extendedM[j][col]*myFrac(-1,1)* k for k in extendedM[col]]
                extendedM[j] =  [x + y for x, y in zip(extendedM[j], sumRow)]       
    res = []
    for ijk in extendedM:
        res.append(ijk[nrows:])
    for ey in res:
        for eyy in ey:
            eyy.simplySelf()
    return res
def getIn(m):
    nrows = len(m)
    ncols = len(m)
    if nrows != ncols:
        raise Exception('Should be square matrix')
    #maybe some further checks someday    
    inverted = gaussInvert(m)
    return inverted
def matmult(a,b):
    zip_b = zip(*b)
    # uncomment next line if python 3 : 
    # zip_b = list(zip_b)
    return [[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b)) 
             for col_b in zip_b] for row_a in a]   
def getRowSol(row):
    lcm = 1
    for i in row:
        lcm *= i.down // gcd(lcm, i.down)
    res = [x.up * (lcm / x.down)  for x in row]
    res.append(lcm)
    return res



M = [[0,2,1,0,0],
    [0,0,0,3,4],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]]

testM = [[myFrac(1,1), myFrac(2,1), myFrac(-1,1)],
            [myFrac(2,1), myFrac(7,1), myFrac(2,1)],
            [myFrac(20,1),myFrac(2,1),myFrac(0,1)]]

Mown, absStates = prepMatrix3(M)
print('matrix prepared')
printMatrix(Mown)
mQ, mR = defineSubM1(Mown, absStates[0])
print('Q')
printMatrix(mQ)
iq = ISubsQ(mQ)
print('I-Q')
printMatrix(iq)
mN = getIn(iq)
print('N')
printMatrix(mN)
print('B')
mB = matmult(mN, mR)
for ey in mB:
        for eyy in ey:
            eyy.simplySelf()
printMatrix(mB)


finalres = getRowSol(mB[0])
print(finalres)   




def solution(m):
    for i in m:
        print (i)
    return 1
   



