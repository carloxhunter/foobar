# Task 3
## Subtask 2

Find the lowest number posible of steps to get from N number to 1.
You can only move by adding/substracting 1 or dividing the current number in 2.

Example: 
- solution(4) returns 2: 4 -> 2 -> 1
- solution(15) returns 5: 15 -> 16 -> 8 -> 4 -> 2 -> 1

Beware that the input is a string, which can be up to 309 characters therefore perfomance is important. I solved in 2 ways with while loop (passed all test) and recursive, this one give the result but with big numbers gets broken. But the logic is still right so i kept it in the repo.

### Detailed Desc:
Commander Lambda has asked for your help to refine the automatic quantum antimatter fuel injection system for her LAMBCHOP doomsday device. It’s a great chance for you to get a closer look at the LAMBCHOP - and maybe sneak in a bit of sabotage while you’re at it - so you took the job gladly.

Quantum antimatter fuel comes in small pellets, which is convenient since the many moving parts of the LAMBCHOP each need to be fed fuel one pellet at a time. However, minions dump pellets in bulk into the fuel intake. You need to figure out the most efficient way to sort and shift the pellets down to a single pellet at a time.

The fuel control mechanisms have three operations:

        Add one fuel pellet
        Remove one fuel pellet
        Divide the entire group of fuel pellets by 2 (due to the destructive energy released when a quantum antimatter pellet is cut in half, the safety controls will only allow this to happen if there is an even number of pellets)

Write a function called solution(n) which takes a positive integer as a string and returns the minimum number of operations needed to transform the number of pellets to 1. The fuel intake control panel can only display a number up to 309 digits long, so there won’t ever be more pellets than you can express in that many digits.

    For example:

        solution(4) returns 2: 4 -> 2 -> 1
        solution(15) returns 5: 15 -> 16 -> 8 -> 4 -> 2 -> 1
