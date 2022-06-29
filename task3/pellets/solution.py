
#works 100%
def solution(n):
    #first catch len of n for border cases
    lenN = len(n)
    #if is largen than 309 chars or does not exist or is not a number (at all) returns 0
    #even tho instructions doesnt explicit say what to return here
    if lenN > 309 or lenN < 0 or not n.isdigit(): return 0
    n_int = int(n)
    #should be gt 1
    if n_int <=1:return 0
    #here we can catch if the number is a power of 2
    def isPowerofTwo(n):
        return (n & (n-1)) == 0
    C=0
    #1 is border case, we skip
    while n_int != 1:
        #3 caused strange behavior when called solution(25) therefore
        #is hardcoded to add 2 and break (this works)
        if n_int == 3:
            C+=2
            break
        #if is divisible by 2 then is the optimal
        elif n_int % 2 == 0:
            n_int = n_int / 2
        #is is not we check if one more or one less is power of 2 which would be 2nd optimal choice
        elif isPowerofTwo(n_int+1):
            n_int+=1
        elif isPowerofTwo(n_int-1):
            n_int-=1
        else:
            mas=n_int+1
            menos=n_int-1
            #we just set if the number is divisible by 4 which ensures us
            #that next one is even, which is good
            if mas % 4 == 0:
                n_int=mas
            elif menos % 4 == 0:
                n_int=menos
            #aoc
            else:
                n_int=menos
        C+=1
    return C


#dictTest = {}
#key=2
#if key in dictTest: print(dictTest[key])
#else: print("{}")
nL='124480579411363943422977485485450829978158403576349485507396127987323092328068524587695005561434534623452345436346456353425362283769712245781118297614280332424240701048410620648401132628401374562794562558123463462235342526466804149296501029546541499918765438784295157088047123009825235235168758962399'
largenine = '9'*310
#print(largenine)
n='4'
x=solution(n)
print(n, x)


