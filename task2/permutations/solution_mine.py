import itertools
test_List1 = [3, 1, 4, 1]
test_List2 = [3, 1, 4, 1, 5, 9]

def solution(l):
    Sols = []
    N = len(l)
    C = 0
    #comb_dict = {N:set(itertools.permutations(l))}
    comb_dict = {}
    def leqSol(N,Sols):
        if (len(Sols) >= 0):
            #maxD = len(str(max[x for x in Sols]))
            maxD = 0
            for item in Sols:
                var = len(str(item))
                if var >= maxD: maxD = var
            return False if N < maxD else True 
        return True

        #while we still have numbers to loops in or
        #while we dont have greater solutions in our Sols list..

    def findDivin3(S):
        L = []
        for item in S:
            sumD = sum(item)
            #print(sumD%3)
            if sumD%3 == 0: 
                strN = ''
                for n in item:
                    strN+=str(n)
                L.append(int(strN))
        return max(L)
    

    #while N > 0 and C <=100:
    #    actual_set = comb_dict[N]
    #    maxD = findDivin3(actual_set)
    #    Sols.append(maxD)

        
    #    C +=1
    #    if len(Sols) >= 0:break
    
    #gen our dic
    original_numbers = {}
    while N>0 and C <=100:
        print('iter',N)
        if (N == len(l)):
            
            original_numbers[N] = [l]
        else:
            if N+1 in original_numbers:
                prevListofNumbers = original_numbers[N+1]
                for listitem in prevListofNumbers:
                    for j in range(len(listitem)):
                        newList = [x for i,x in enumerate(listitem) if i!=j]
                        print(newList)
                    #print('iter', N,listitem)
                #print(original_numbers[N+1])    
        N -=1
        C +=1

    print('final: ',original_numbers)
    if len(Sols)>0 :
        return max(Sols)
    else: return 0

    

print(solution(test_List1))

