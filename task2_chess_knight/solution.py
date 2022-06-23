
def getIntFromCoordinates(x,y):
    if x < 0 or x > 7:
        return None
    if y < 0 or y > 7:
        return None
    return 8*y+x
def getCoordinatesFromInteger(N):
    if N < 0 or N > 63:
        return None
    y=N//8
    x=N-8*y
    return (x,y)
#at the very end neightbors distance is always 3 due knight movement.. therefore its ommited
def getDistanceAdjacent(x1,x2,y1,y2):
    return abs(x1-x2)+abs(y1-y2)
def getGeomDistanceH(x1,y1,x2,y2):
   dx=x2-x1
   dy=y2-y1
   return dx*dx + dy*dy 
def getKnightNeighbors(x,y,xd,yd):
    neighbors=[]
    if x+1 <= 7:
        if y+2 <= 7:
            neighbors.append((x+1,y+2,getGeomDistanceH(xd,yd,x+1,y+2)))
        if y-2 >= 0:
            neighbors.append((x+1,y-2,getGeomDistanceH(xd,yd,x+1,y-1)))
    if x-1 >= 0:
        if y+2 <= 7:
            neighbors.append((x-1,y+2,getGeomDistanceH(xd,yd,x-1,y+2)))
        if y-2 >= 0:
            neighbors.append((x-1,y-2,getGeomDistanceH(xd,yd,x-1,y-2)))
    if x+2 <=7:
        if y+1<=7:
            neighbors.append((x+2,y+1,getGeomDistanceH(xd,yd,x+2,y+1)))
        if y-1 >= 0:
            neighbors.append((x+2,y-1,getGeomDistanceH(xd,yd,x+2,y-1)))
    if x-2 >= 0:
        if y+1<=7:
            neighbors.append((x-2,y+1,getGeomDistanceH(xd,yd,x-2,y+1)))
        if y-1 >= 0:
            neighbors.append((x-2,y-1,getGeomDistanceH(xd,yd,x-2,y-1)))
    return neighbors

def customListMin(L):
    minxy = (-1,-1,10000)
    for xy in L:
        if xy[2] <= minxy[2]:
            minxy = xy
    return minxy


#print(getIntFromCoordinates(1,2))
#print(getIntFromCoordinates(-1,20))
#print(getCoordinatesFromInteger(17))
#print(getCoordinatesFromInteger(63))
#for i in range(0,64):
#    print(i, getCoordinatesFromInteger(i))
#print(getKnightNeighbors(4,4))
#print(getGeomDistanceH(1,1,2,2))

class Node:
    def __init__(self,x,y,xd,yd):
        self.x=x
        self.y=y
        self.xd=xd
        self.yd=yd
        self.hd = getGeomDistanceH(x,y,xd,yd)
        self.neighbors = getKnightNeighbors(x,y,xd,yd)
        self.closerNeighbor = customListMin(self.neighbors)
    def print(self):
        print(self.x,self.y,self.hd,self.neighbors,self.closerNeighbor)
    def update(self,x,y,xd,yd):
        self.x=x
        self.y=y
        self.hd = getGeomDistanceH(x,y,xd,yd)
        self.neighbors = getKnightNeighbors(x,y,xd,yd)
        self.closerNeighbor = customListMin(self.neighbors)
    def isDestiny(self):
        return self.x == self.xd and self.y == self.yd

sx,sy,dx,dy = 1,1,2,2
N = Node(sx,sy,dx,dy)

count = 0
openL = []
closedL= []
openL.append((0,sx,sy))

def genGrid(dimx,dimy):
    count=0
    M = []
    for x in range(dimx):
        Mtemp = []
        for y in range(dimy):
            Mtemp.append(count)
            count+=1
        M.append(Mtemp)
    return M

def genDict(dimx,dimy):
    D={}
    for i in range(dimx*dimy):
        #cords, g_score, f_score, h_score
        D[i]=(getCoordinatesFromInteger(i), 999, None)
    return D

def genList(dimx,dimy):
    L=[]
    for i in range(dimx*dimy):
        #cords, g_score, f_score, h_score
        L.append(getCoordinatesFromInteger(i))
    return L



    #def print(self):
    #    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
    #  for row in self.grid]))
    

#GT.print()
#print(GT.dict)


def getKnightNeighbors2(x,y, unvisitedL):
    neighbors=[]
    x_ = x+1
    if x_ <= 7:
        y_ = y+2
        if y_ <= 7 and (x_,y_) in unvisitedL:
            neighbors.append((x_,y_,))
        y_ = y-2
        if y_ >= 0 and (x_,y_) in unvisitedL:
            neighbors.append((x+1,y-2,))
    x_ = x-1
    if x_ >= 0:
        y_ = y+2
        if y_ <= 7 and (x_,y_) in unvisitedL:
            neighbors.append((x_,y_,))
        y_=y-2
        if y-2 >= 0 and (x_,y_) in unvisitedL:
            neighbors.append((x_,y_,))
    x_=x+2
    if x_ <=7:
        y_=y+1
        if y_<=7 and (x_,y_) in unvisitedL:
            neighbors.append((x_,y_,))
        y_=y-1
        if y_ >= 0 and (x_,y_) in unvisitedL:
            neighbors.append((x_,y_,))
    x_=x-2
    if x_ >= 0:
        y_=y+1
        if y_<=7 and (x_,y_) in unvisitedL:
            neighbors.append((x_,y_,))
        y_=y-1
        if y_ >= 0 and (x_,y_) in unvisitedL:
            neighbors.append((x_,y_,))
    return neighbors


class Grid:
    def __init__(self,dimx,dimy) -> None:
        self.visited = []
        self.unvisited = genList(dimx,dimy)
        self.dict = genDict(dimx, dimy)
    def unfinished(self):
        return len(self.unvisited) > 0 
    def setStart(self, N):
        self.dict[N] = (getCoordinatesFromInteger(N), 0, None)
    def getSDS(self):
        someTuple = (None,999999999,None)
        for key, value in self.dict.items():
            if  value[1] < someTuple[1]:
                someTuple = value
        return someTuple


class Node2:
    def __init__(self,x0,y0):
        self.id=getIntFromCoordinates(x0,y0)
        self.x, self.y = x0,y0
        self.prevNode = None
        self.prevNodeDist = 99999
        self.unvisitedNeighbors = []
    def updateCoords(self,x0,y0):
        self.id=getIntFromCoordinates(x0,y0)
        self.x, self.y = x0,y0
        self.prevNode = None
        self.prevNodeDist = 99999
        self.unvisitedNeighbors = []
    def getUnvisitedNeighbors(self, unvisitedL):
        self.unvisitedNeighbors = getKnightNeighbors2(self.x,self.y,unvisitedL)
    def printSelf(self):
        print('currentNode: ',self.id, self.x,self.y,self.prevNode,self.prevNodeDist)
        print('unvisited neighbors:' ,self.unvisitedNeighbors)
    
    
GT = Grid(8,8)
#print(GT.unvisited,GT.visited,GT.dict)
count=0    
init = 8
dest = 27
initx,inity = getCoordinatesFromInteger(init)
GT.setStart(init)
#currentNode = Node2(init)
while GT.unfinished():
    #currentNode.getUnvisitedNeighbors(GT.unvisited)
    #print(count)
    #print(currentNode.x,currentNode.y,currentNode.unvisitedNeighbors)

   
    current = GT.getSDS()
    print('current: ',current)
    x,y = current[0]
    currentNode = Node2(x,y)
    currentNode.getUnvisitedNeighbors(GT.unvisited)
    currentNode.printSelf()



    
    
    count+=1
    if count > 1: break


#print(GT.dict)
#print(GT.getSDS())
    
