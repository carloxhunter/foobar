
def getIntFromCoordinates(x,y):
    if x < 0 or x > gridSize-1:
        return None
    if y < 0 or y > gridSize-1:
        return None
    return gridSize*y+x
def getCoordinatesFromInteger(N):
    if N < 0 or N > gridSize*gridSize-1:
        return None
    y=N//gridSize
    x=N-gridSize*y
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

def getKnightNeighbors3(x,y, dicto):
    neighbors=[]
    x_ = x+1
    if x_ <= gridSize-1:
        y_ = y+2
        id = getIntFromCoordinates(x_,y_)
        if y_ <= gridSize-1 and not dicto[id].visited:
            neighbors.append((x_,y_,))
        y_ = y-2
        id = getIntFromCoordinates(x_,y_)
        if y_ >= 0 and not dicto[id].visited:
            neighbors.append((x+1,y-2,))
    x_ = x-1
    if x_ >= 0:
        y_ = y+2
        id = getIntFromCoordinates(x_,y_)
        if y_ <= gridSize-1 and not dicto[id].visited:
            neighbors.append((x_,y_,))
        y_=y-2
        id = getIntFromCoordinates(x_,y_)
        if y_ >= 0:
            neighbors.append((x_,y_,))
    x_=x+2
    if x_ <=gridSize-1:
        y_=y+1
        id = getIntFromCoordinates(x_,y_)
        if y_<=gridSize-1 and not dicto[id].visited:
            neighbors.append((x_,y_,))
        y_=y-1
        id = getIntFromCoordinates(x_,y_)
        if y_ >= 0 and not dicto[id].visited:
            neighbors.append((x_,y_,))
    x_=x-2
    if x_ >= 0:
        y_=y+1
        id = getIntFromCoordinates(x_,y_)
        if y_<=gridSize-1 and not dicto[id].visited:
            neighbors.append((x_,y_,))
        y_=y-1
        id = getIntFromCoordinates(x_,y_)
        if y_ >= 0 and not dicto[id].visited:
            neighbors.append((x_,y_,))
    return neighbors

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
        
        #cords, diststart, previousNeighboor, visited
        #D[i]=(getCoordinatesFromInteger(i), 999, None, False)
        x,y=getCoordinatesFromInteger(i)
        #print(i,x,y)
        
       
        D[i]=Node2(x,y)
    return D

def genList(dimx,dimy):
    L=[]
    for i in range(dimx*dimy):
        #cords, g_score, f_score, h_score
        L.append(getCoordinatesFromInteger(i))
    return L


class Node2:
    def __init__(self,x0,y0):
        self.id=getIntFromCoordinates(x0,y0)
        self.x, self.y = x0,y0
        self.prevNode = None
        self.prevNodeDist = 99999
        self.unvisitedNeighbors = []
        self.visited = False
    def updateCoords(self,x0,y0):
        self.id=getIntFromCoordinates(x0,y0)
        self.x, self.y = x0,y0
        self.prevNode = None
        self.prevNodeDist = 99999
        self.unvisitedNeighbors = []
        self.visited = False
    def setVisited(self):
        self.visited=True
    def setStarter(self):
        self.prevNodeDist=0
    def getUnvisitedNeighbors(self, dicto):
        #self.unvisitedNeighbors = getKnightNeighbors2(self.x,self.y,unvisitedL)
         self.unvisitedNeighbors =  getKnightNeighbors3(self.x,self.y, dicto)

    def updateStatus(self, dist, prev):
        self.prevNode = prev
        self.prevNodeDist = dist
    def printSelf(self):
        #print('id:',self.id, 'x:',self.x,'y:',self.y,'prevNode:',self.prevNode,
        #'prevNodeDist:', self.prevNodeDist, 'visited:',self.visited,
        #'unvisited neighbors:' ,self.unvisitedNeighbors)
        print('id:',self.id, 'x:',self.x,'y:',self.y,'prevNode:',self.prevNode,
        'prevNodeDist:', self.prevNodeDist, 'visited:',self.visited)
    def printSelfAll(self):
        print('id:',self.id, 'x:',self.x,'y:',self.y,'prevNode:',self.prevNode,
        'prevNodeDist:', self.prevNodeDist, 'visited:',self.visited,
        'unvisited neighbors:' ,self.unvisitedNeighbors)
    def updateMatrix(self, dicto):
        #we already know as is not weighted that the distances are all 3.. therefore they will be 1
        #since AX = 0 => X=0 by linear algebra
        if len(self.unvisitedNeighbors) > 0:
            for node in self.unvisitedNeighbors:
                id = getIntFromCoordinates(node[0],node[1])
                #if previous distance to the point is bigger than 1 (every step will  be 1)
                #plus the previous distance from the actual point to start, then we replace
                val = 1 + self.prevNodeDist
                if dicto[id].prevNodeDist > val:
                    dicto[id].updateStatus(val, self.id)

class Grid:
    def __init__(self,dimx,dimy) -> None:
        self.dicto = genDict(dimx, dimy)
        self.start = None
        self.dest = None
        self.path = []
    def finished(self):
        for item in self.dicto.values():
            if not item.visited:
                return False
        return True
    def config(self, start,dest):
        self.start = start
        self.dest = dest
        self.dicto[start].setStarter()
    def getSDS(self):
        previd = -1
        prevval = 9999999
        for key, value in self.dicto.items():
            #if  value.prevNodeDist < prevval:
            #value.printSelf()
            #print(value.prevNodeDist, value.printSelf(), key)
            if value.prevNodeDist < prevval and value.visited == False:
                prevval = value.prevNodeDist
                previd = key
        if key == -1:
            return None
        return self.dicto[previd]
    def printSelf(self):
        for item in self.dicto.values():
            item.printSelf()
    def printSelfAll(self):
        for item in self.dicto.values():
            item.printSelfAll()
    def getPath(self):
        tempPath = []
        tempNode = self.dicto[self.dest]
        while tempNode.id != self.start:
            print(tempNode.id)
            tempPath.append(tempNode)
            tempNode = self.dicto[tempNode.prevNodeDist]
        self.path=tempPath.reverse()
    def printPath(self):return

gridSize = 8
GT = Grid(gridSize,gridSize)
#print(GT.unvisited,GT.visited,GT.dict)
count=0    
init = 0
dest = 1
initx,inity = getCoordinatesFromInteger(init)
GT.config(init,dest)

while not GT.finished():
    print('iter', count)  
    current = GT.getSDS()
    current.getUnvisitedNeighbors(GT.dicto)
    current.updateMatrix(GT.dicto)
    current.setVisited()
    current.printSelfAll()
    count+=1
    if count > 100 or current == None: break
GT.printSelfAll() 
 #ok   
#GT.printSelf()
#ok
#print('iter1')
#current = GT.getSDS()
#current.getUnvisitedNeighbors(GT.dicto)
#current.printSelfAll()
#current.updateMatrix(GT.dicto)
#current.setVisited()
#GT.printSelfAll() 

#print('iter2')
#current = GT.getSDS()
#current.getUnvisitedNeighbors(GT.dicto)
#current.printSelfAll()
#current.updateMatrix(GT.dicto)
#current.setVisited()
#GT.printSelfAll() 

#current.getUnvisitedNeighbors(GT.dicto)
#current.updateMatrix(GT.dicto)
#current.setVisited()

#current = GT.getSDS()
#print('newcurrent')
#current.printSelfAll()
#print('final')
#GT.printSelf()
#print('antes getpath')
#GT.getPath()
#print(init,dest,GT.path)