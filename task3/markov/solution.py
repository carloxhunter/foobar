 
def solution(m):
    #gdc https://stackoverflow.com/questions/11175131/code-for-greatest-common-divisor-in-python
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
        #simplify https://stackoverflow.com/questions/37237954/calculate-the-lcm-of-a-list-of-given-numbers-in-python
        def getsimplify(self):
            gcdd = gcd(self.up, self.down)
            return myFrac(self.up / gcdd, self.down / gcdd)
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
        #just observed how matrixcalc did it and replicated the steps
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
        #thanks to akavall
        #https://stackoverflow.com/questions/10508021/matrix-multiplication-in-pure-python
        zip_b = zip(*b)
        return [[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b)) 
                for col_b in zip_b] for row_a in a]   
    def getRowSol(row):
        lcm = 1
        for i in row:
            lcm *= i.down // gcd(lcm, i.down)
        res = [x.up * (lcm / x.down)  for x in row]
        res.append(lcm)
        #found out that idk what part of proccess the number  in some tries was set to L
        #while clearly a number < fit on integer
        #so made this 'dirty trick' to 'solve' it
        #res = [str(x) for x in res]
        #res = [int(x) for x in res]
        return res
    def getCanonicalForm4(m):
        trans = []
        absorbs = []
        sumT = []
        for idrow, row in enumerate(m):
            if sum(row) == 0:
                absorbs.append(idrow)
            else:
                sumT.append(sum(row))
                trans.append(idrow)
        mQ = []
        mR = []
        for idt, t1 in enumerate(trans):
            mQt = []
            mRt = []
            for t2 in trans:
                nv = myFrac(m[t1][t2],sumT[idt])
                mQt.append(nv)
            for ab in absorbs:
                nv = myFrac(m[t1][ab],sumT[idt])
                mRt.append(nv)
            mQ.append(mQt)
            mR.append(mRt)
        
        return mQ, mR
    #actual process
    #check if is empty
    if (len(m) == 0):
        return []
    #check if has 1 state only
    if(len(m) == 1):
        return [1,1]
    #check if state 0 is terminal, i.e all will fall here
    if(sum(m[0]) == 0):
        sl=[]
        for x in m:
            sl.append(0)
        sl[0]=1
        sl[-1]=1
        return sl
    mQ, mR = getCanonicalForm4(m)
    iq = ISubsQ(mQ)
    mN = getIn(iq)
    mB = matmult(mN, mR)
    #just simplify the matrix
    for ey in mB:
        for eyy in ey:
            eyy.simplySelf()
    finalres = getRowSol(mB[0])
    return finalres








