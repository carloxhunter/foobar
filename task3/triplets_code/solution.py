def solution(l):
    #if our lenght cant make a triplet instantly return 0
    if len(l) < 3: return 0
    #initianilize all our dict values in 0
    #we store the amount of way it can be divided the i-th number
    default_val = 0
    mem_dict = dict.fromkeys(range(0,len(l)),default_val)
    #we only need number of combinations, not them so just store a counter
    C=0
    for idxmain, main in enumerate(l):
        #we only need to look from start to our current point
        for idxcurrent, current in enumerate(l[:idxmain]):
            #we skip if is the same index (aka same sumber)
            #fulfill our conditions
            if idxmain != idxcurrent and main % current == 0:
                #if our main number can be divided by the actual one on the loop
                #then we add to our counter the number of ways we can divide it
                #with our previous history
                C+= mem_dict[idxcurrent]
                #if can be divided by this number we update our index counter cause
                #we added one more conbination
                mem_dict[idxmain] += 1
    return C


test1=[1,1,1]
test2=[1,2,3,4,5,6]
test3=[4, 5, 2, 8, 5, 9, 2, 2, 7, 1]
test4=[1,1,1,1]
test5 = [x for x in range(1,999)]

selected_test=test5
print(solution(selected_test))



