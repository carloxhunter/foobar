def solution(src, dest):
    def getIntFromCoordinates(x, y):
        if x < 0 or x > gridSize-1:
            return None
        if y < 0 or y > gridSize-1:
            return None
        return gridSize*y+x

    def getCoordinatesFromInteger(N):
        if N < 0 or N > gridSize*gridSize-1:
            return None
        y = N//gridSize
        x = N-gridSize*y
        return (x, y)

    def getKnightNeighbors3(x, y, dicto):
        neighbors = []
        x_ = x+1
        if x_ <= gridSize-1:
            y_ = y+2
            id = getIntFromCoordinates(x_, y_)
            if y_ <= gridSize-1 and not dicto[id].visited:
                neighbors.append((x_, y_,))
            y_ = y-2
            id = getIntFromCoordinates(x_, y_)
            if y_ >= 0 and not dicto[id].visited:
                neighbors.append((x+1, y-2,))
        x_ = x-1
        if x_ >= 0:
            y_ = y+2
            id = getIntFromCoordinates(x_, y_)
            if y_ <= gridSize-1 and not dicto[id].visited:
                neighbors.append((x_, y_,))
            y_ = y-2
            id = getIntFromCoordinates(x_, y_)
            if y_ >= 0:
                neighbors.append((x_, y_,))
        x_ = x+2
        if x_ <= gridSize-1:
            y_ = y+1
            id = getIntFromCoordinates(x_, y_)
            if y_ <= gridSize-1 and not dicto[id].visited:
                neighbors.append((x_, y_,))
            y_ = y-1
            id = getIntFromCoordinates(x_, y_)
            if y_ >= 0 and not dicto[id].visited:
                neighbors.append((x_, y_,))
        x_ = x-2
        if x_ >= 0:
            y_ = y+1
            id = getIntFromCoordinates(x_, y_)
            if y_ <= gridSize-1 and not dicto[id].visited:
                neighbors.append((x_, y_,))
            y_ = y-1
            id = getIntFromCoordinates(x_, y_)
            if y_ >= 0 and not dicto[id].visited:
                neighbors.append((x_, y_,))
        return neighbors

    def genDict(dimx, dimy):
        D = {}
        for i in range(dimx*dimy):
            x, y = getCoordinatesFromInteger(i)
            D[i] = Node2(x, y)
        return D

    class Node2:
        def __init__(self, x0, y0):
            self.id = getIntFromCoordinates(x0, y0)
            self.x, self.y = x0, y0
            self.prevNode = None
            self.prevNodeDist = 99999
            self.unvisitedNeighbors = []
            self.visited = False

        def updateCoords(self, x0, y0):
            self.id = getIntFromCoordinates(x0, y0)
            self.x, self.y = x0, y0
            self.prevNode = None
            self.prevNodeDist = 99999
            self.unvisitedNeighbors = []
            self.visited = False

        def setVisited(self):
            self.visited = True

        def setStarter(self):
            self.prevNodeDist = 0

        def getUnvisitedNeighbors(self, dicto):
            self.unvisitedNeighbors = getKnightNeighbors3(
                self.x, self.y, dicto)

        def updateStatus(self, dist, prev):
            self.prevNode = prev
            self.prevNodeDist = dist

        def printSelf(self):
            print('id:', self.id, 'x:', self.x, 'y:', self.y, 'prevNode:', self.prevNode,
                  'prevNodeDist:', self.prevNodeDist, 'visited:', self.visited)

        def printSelfAll(self):
            print('id:', self.id, 'x:', self.x, 'y:', self.y, 'prevNode:', self.prevNode,
                  'prevNodeDist:', self.prevNodeDist, 'visited:', self.visited,
                  'unvisited neighbors:', self.unvisitedNeighbors)

        def updateMatrix(self, dicto):
            # we already know as is not weighted that the distances are all 3.. therefore they will be 1
            # since AX = 0 => X=0 by linear algebra
            if len(self.unvisitedNeighbors) > 0:
                for node in self.unvisitedNeighbors:
                    id = getIntFromCoordinates(node[0], node[1])
                    # if previous distance to the point is bigger than 1 (every step will  be 1)
                    # plus the previous distance from the actual point to start, then we replace
                    val = 1 + self.prevNodeDist
                    if dicto[id].prevNodeDist > val:
                        dicto[id].updateStatus(val, self.id)

    class Grid:
        def __init__(self, dimx, dimy):
            self.dicto = genDict(dimx, dimy)
            self.start = None
            self.dest = None
            self.path = []

        def finished(self):
            for item in self.dicto.values():
                if not item.visited:
                    return False
            return True

        def config(self, start, dest):
            self.start = start
            self.dest = dest
            self.dicto[start].setStarter()

        def getSDS(self):
            previd = -1
            prevval = 9999999
            for key, value in self.dicto.items():
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
                tempPath.append(tempNode.id)
                tempNode = self.dicto[tempNode.prevNode]
            self.path = tempPath

        def printPath(self):
            print(self.path)

        def getMinPath(self):
            return len(self.path)

    gridSize = 8
    GT = Grid(gridSize, gridSize)
    GT.config(src, dest)
    while not GT.finished():
        current = GT.getSDS()
        current.getUnvisitedNeighbors(GT.dicto)
        current.updateMatrix(GT.dicto)
        current.setVisited()
    GT.getPath()
    return GT.getMinPath()

print(solution(0,1))