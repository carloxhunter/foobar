
#works well but at big numbers its recursion kills python stack
def solution(n):
    lenN = len(n)
    if lenN > 309 or lenN < 0 or not n.isdigit(): return 0
    n_int = int(n)
    if n_int <=0:return 0
    dp = {}
    def func(n_int, dp):
        if  n_int <= 0:
            return 0
        elif n_int in dp:
            return dp[n_int]
        elif n_int == 1:
            dp[n_int]=0 
            return 0
        elif n_int == 2:
            dp[n_int]=1
            return 1
        else:
            if(n_int%2==0):
                val2=min(n_int-1,func(n_int/2,dp))+1
                dp[n_int]=val2
                return val2
            else:
                #val31=func(n_int-1,dp)
                #val32=func(n_int+1,dp)
                val3=min(n_int-1,func(n_int-1,dp), func(n_int+1,dp))+1
                dp[n_int]=val3
                return val3       
    func(n_int,dp)      
    return dp[n_int]


#dictTest = {}
#key=2
#if key in dictTest: print(dictTest[key])
#else: print("{}")
n='124480579411363943422977485485450829978158403576349485507396127987323092328068524587695005561434534623452345436346456353425362283769712245781118297614280332424240701048410620648401132628401374562794562558123463462235342526466804149296501029546541499918765438784295157088047123009825235235168758962399'
x=solution(n)
print(x)