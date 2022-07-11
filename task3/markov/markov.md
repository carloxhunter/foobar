For example, consider the matrix m:
[
  [0,1,0,0,0,1],  # s0, the initial state, goes to s1 and s5 with equal probability
  [4,0,0,3,2,0],  # s1 can become s0, s3, or s4, but with different probabilities
  [0,0,0,0,0,0],  # s2 is terminal, and unreachable (never observed in practice)
  [0,0,0,0,0,0],  # s3 is terminal
  [0,0,0,0,0,0],  # s4 is terminal
  [0,0,0,0,0,0],  # s5 is terminal
]
So, we can consider different paths to terminal states, such as:
s0 -> s1 -> s3
s0 -> s1 -> s0 -> s1 -> s0 -> s1 -> s4
s0 -> s1 -> s0 -> s5
Tracing the probabilities of each, we find that
s2 has probability 0
s3 has probability 3/14
s4 has probability 1/7
s5 has probability 9/14
So, putting that together, and making a common denominator, gives an answer in the form of
[s2.numerator, s3.numerator, s4.numerator, s5.numerator, denominator] which is
[0, 3, 2, 9, 14].


absorving markovs
http://www.dim.uchile.cl/~mkiwi/ma34a/libro/ch11.pdf
Gcd
https://stackoverflow.com/questions/11175131/code-for-greatest-common-divisor-in-python
simplify
https://stackoverflow.com/questions/37237954/calculate-the-lcm-of-a-list-of-given-numbers-in-python

#i was struggin with this one for about 4 days to work proberly
    #triying to order the big Matrix.. given a 2nd..3rd..4th try i realized
    #is not nescesary to reorder it.. you just have to take the probs
    # (or quantities here) from each transitory and absorving state and order them
    #Q: Trans to Trans, R: Trans to Absorb
    #thanks https://www.youtube.com/watch?v=BsOkOaB8SFk

