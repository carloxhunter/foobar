 
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
        res = [str(x) for x in res]
        res = [int(x) for x in res]
        return res
    #col swapper https://stackoverflow.com/questions/69803358/swapping-columns-of-a-matrix-without-numpy
    def col_swapper(matrix, col_1, col_2):
        for line in range(len(matrix)):
            matrix[line][col_1], matrix[line][col_2] = matrix[line][col_2], matrix[line][col_1]
    def row_swapper(matrix, row1,row2):
        for col in range(len(matrix)):
            matrix[row1][col], matrix[row2][col] = matrix[row2][col], matrix[row1][col]
    def getCanonicalForm2(m):
        #understanding of it : https://www.youtube.com/watch?v=BsOkOaB8SFk
        trans = []
        for i, val in enumerate(m):
            if sum(val) > 0:
                trans.append(i)
        for idx_in_list, idx_in_matrix in enumerate(trans):
            col_swapper(m,idx_in_list,idx_in_matrix)
            row_swapper(m,idx_in_list,idx_in_matrix)
        return m   
    #actual process
    #check if is empty
    if (len(m) == 0):
        return []
    #check if has 1 state only
    if(len(m) == 1):
        return [1,1]
    #get canonical form
    getCanonicalForm2(m)
    #set myFrac class to the actual matrix to work with
    Mown, absStates = prepMatrix3(m)   
    mQ, mR = defineSubM1(Mown, absStates[0])
    iq = ISubsQ(mQ)
    mN = getIn(iq)
    mB = matmult(mN, mR)
    #just simplify the matrix
    for ey in mB:
        for eyy in ey:
            eyy.simplySelf()
    finalres = getRowSol(mB[0])
    return finalres



from gigachad import *  


M = M54  
R = R54 


sol = solution(M)
print(sol)
print(R)




