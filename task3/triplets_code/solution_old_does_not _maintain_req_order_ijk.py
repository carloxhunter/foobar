

#LT = [1,1,1]
#a=itertools.combinations(LT,3)
#print(a)

#c=0

#forloop calls all these automatically
#iterA= iter(a)
#print(iterA.next())
#print(iterA.next())
def accomplishConds(L, prev):
    for i in L[1:]:
        if i % prev == 0 and i >= prev:
            yield True
        else: yield False
#C = 0
#for x in a:
#    print(x)
#    prev = x[0]
#    flag = True
#    for y in x[1:]:
#        print(y)
#        if y % prev == 0 and y >= prev:
#            print('si')
#        else: 
#            print('no')
#            flag = False
#        print('prev',prev,'actual',y)
#        prev = y
#    if flag: C+=1

#print(C)

def solution(l):
    #we only need number of combinations, not them so just store a counter
    C=0
    import itertools
    #std lib, here's the implementation of combinations.. returns a generator
    #therefore we can iterate through without storing the values on memory
    #https://docs.python.org/3/library/itertools.html#itertools.combinations
    comb_generator = itertools.combinations(l,3)
    #iter in comb
    for triplet in comb_generator:
        #we store the first (prev value)
        prev=triplet[0]
        #set our flag
        flag=True
        #loop only over the 2 and 3 pos since we have already the first
        for y in triplet[1:]:
            #if meets our lucky conditions
            if y % prev == 0 and y >= prev:
                pass
            #if not then set our flag in false
            else:
                flag = False    
            #update the previous number to the actual one
            prev = y
        #check if our flag is true -> if our tuple accomplish what we need
        if flag : C += 1
    return C

#print(solution([1,2,3,4,5,6]))
#print(solution([1,1,1]))
test_long = [x for x in range(1,999)]

sol = solution(test_long)
print(sol)


